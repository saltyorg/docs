"""Keep generator-only tagged examples out of MkDocs metadata construction."""

from __future__ import annotations

from collections.abc import Iterator

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.utils.meta import YAML_RE
from yaml.nodes import MappingNode, Node, SequenceNode
from yaml.resolver import BaseResolver


EXAMPLE_PATH = ("saltbox_automation", "inventory", "example_overrides")


def on_page_read_source(page, config, **kwargs):
    """Remove unsupported tagged examples from the in-memory metadata source."""
    del config, kwargs
    source = page.file.content_string
    match = YAML_RE.match(source)
    if match is None:
        return None

    path = page.file.src_path
    try:
        document = yaml.compose(match.group(1), Loader=yaml.SafeLoader)
    except yaml.YAMLError as error:
        raise PluginError(f"{path}: parsing YAML frontmatter: {error}") from error

    binding = _find_mapping_value(document, EXAMPLE_PATH)
    if binding is None:
        return None
    parent, index, examples = binding
    if not isinstance(examples, MappingNode) or not examples.value:
        return None
    if not any(not _safe_loader_supports(node.tag) for node in _walk(examples)):
        return None
    if _shares_nodes_outside_binding(document, parent, index, examples):
        raise PluginError(
            f"{path}: YAML alias crosses the example_overrides metadata boundary"
        )

    parent.value[index] = (
        parent.value[index][0],
        MappingNode(BaseResolver.DEFAULT_MAPPING_TAG, [], flow_style=True),
    )
    try:
        sanitized = yaml.serialize(document)
        yaml.load(sanitized, Loader=yaml.SafeLoader)
    except yaml.YAMLError as error:
        raise PluginError(f"{path}: sanitizing YAML frontmatter: {error}") from error

    return source[: match.start(1)] + sanitized + source[match.end(1) :]


def _find_mapping_value(
    root: Node | None, path: tuple[str, ...]
) -> tuple[MappingNode, int, Node] | None:
    current = root
    for depth, expected in enumerate(path):
        if not isinstance(current, MappingNode):
            return None
        for index, (key, value) in enumerate(current.value):
            if key.value != expected:
                continue
            if depth == len(path) - 1:
                return current, index, value
            current = value
            break
        else:
            return None
    return None


def _safe_loader_supports(tag: str) -> bool:
    if tag in yaml.SafeLoader.yaml_constructors:
        return True
    return any(tag.startswith(prefix) for prefix in yaml.SafeLoader.yaml_multi_constructors)


def _walk(root: Node) -> Iterator[Node]:
    pending = [root]
    seen: set[int] = set()
    while pending:
        node = pending.pop()
        if id(node) in seen:
            continue
        seen.add(id(node))
        yield node
        pending.extend(_children(node))


def _children(node: Node) -> list[Node]:
    if isinstance(node, MappingNode):
        return [child for pair in node.value for child in pair]
    if isinstance(node, SequenceNode):
        return list(node.value)
    return []


def _shares_nodes_outside_binding(
    document: Node | None,
    binding_parent: MappingNode,
    binding_index: int,
    examples: Node,
) -> bool:
    if document is None:
        return False
    example_nodes = {id(node) for node in _walk(examples)}
    pending = [document]
    seen: set[int] = set()
    while pending:
        node = pending.pop()
        if id(node) in example_nodes:
            return True
        if id(node) in seen:
            continue
        seen.add(id(node))
        if isinstance(node, MappingNode):
            for index, (key, value) in enumerate(node.value):
                pending.append(key)
                if node is binding_parent and index == binding_index:
                    continue
                pending.append(value)
        elif isinstance(node, SequenceNode):
            pending.extend(node.value)
    return False
