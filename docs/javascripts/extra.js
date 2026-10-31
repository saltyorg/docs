// Role Defaults override - scope toggle
function updateToggleDisplay() {
  const toggleCheckbox = document.querySelector('.sb-toggle--override-scope input[type="checkbox"]');
  if (!toggleCheckbox) return;

  const isChecked = toggleCheckbox.checked;

  document.querySelectorAll('.sb-show-on-unchecked').forEach(el => {
    el.style.display = isChecked ? 'none' : 'block';
  });
  document.querySelectorAll('.sb-show-on-checked').forEach(el => {
    el.style.display = isChecked ? 'block' : 'none';
  });
}

// Content tabs - custom background colors
function setActiveTabColor() {
  document.querySelectorAll('.md-typeset .tabbed-set').forEach(tabSet => {
    const inputs = tabSet.querySelectorAll('input[type="radio"]');
    const labels = tabSet.querySelectorAll('.tabbed-labels > label');
    inputs.forEach((input, idx) => {
      if (labels[idx]) {
        if (input.checked) {
          labels[idx].style.backgroundColor = 'color-mix(in srgb, var(--md-primary-fg-color), transparent 70%)';
        } else {
          labels[idx].style.backgroundColor = '';
        }
      }
    });
  });
}

// Delegated listeners: registered once, they keep working across instant navigation
document.addEventListener('click', function (event) {
  if (event.target && event.target.matches('.sb-toggle--override-scope input[type="checkbox"]')) {
    updateToggleDisplay();
  }
});

document.addEventListener('change', function (event) {
  if (event.target.matches('.md-typeset .tabbed-set > input[type="radio"]')) {
    setActiveTabColor();
  }
});

// Per-page setup: runs on every page load / instant navigation
document$.subscribe(function () {
  updateToggleDisplay();
  setActiveTabColor();

  // Open same-origin link to non-markdown page in a new tab
  document.querySelectorAll('a[href]').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href && !href.startsWith('#')) {
      const url = new URL(href, window.location.origin);
      if (url.origin === window.location.origin && /\.[^/]+$/.test(url.pathname)) {
        link.setAttribute('target', '_blank');
      }
    }
  });
});

// Termynal syntax highlighting
(() => {
  if (!window.CSS || !CSS.highlights) return; // older browsers: no coloring

  const SCOPE = '[data-ty=""]'; // output lines (plain data-ty attribute)

  // highlight name -> pattern
  const patterns = {
    'ty-heading':  /^ *[A-Z]+ *$/g,
    'ty-command':  /^ *[a-z][a-z-]+/g,
    'ty-argument': /\[[^\]]+]/g,
    'ty-flag':     /^ *-[a-z- ]+/g,
  };

  function update() {
    const found = Object.fromEntries(Object.keys(patterns).map(k => [k, []]));
    document.querySelectorAll(SCOPE).forEach(line => {
      const walker = document.createTreeWalker(line, NodeFilter.SHOW_TEXT);
      while (walker.nextNode()) {
        const node = walker.currentNode;
        for (const [name, re] of Object.entries(patterns)) {
          for (const m of node.textContent.matchAll(re)) {
            const r = new Range();
            r.setStart(node, m.index);
            r.setEnd(node, m.index + m[0].length);
            found[name].push(r);
          }
        }
      }
    });
    for (const [name, ranges] of Object.entries(found)) {
      CSS.highlights.set(name, new Highlight(...ranges));
    }
  }

  let queued = false;
  new MutationObserver(() => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => { queued = false; update(); });
  }).observe(document.documentElement, { childList: true, characterData: true, subtree: true });

  update();
})();