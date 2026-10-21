const { execFileSync } = require('node:child_process');

const MESSAGE = 'docs: automated documentation update\n\nUpdated by sb-docs automation\n\n🤖 Generated with sb-docs';
const MUTATION = `mutation($input: CreateCommitOnBranchInput!) {
  createCommitOnBranch(input: $input) { commit { oid } }
}`;

module.exports = async function commitGenerated({ github, core, context }) {
  const git = (...args) => execFileSync('git', args, { cwd: 'docs' });
  if (!context.ref.startsWith('refs/heads/')) {
    throw new Error('Documentation commits require a branch');
  }
  const base = git('rev-parse', 'HEAD').toString().trim();
  git('add', '-A', '--', 'docs');
  const changes = git('diff', '--cached', '--name-status', '-z', '--no-renames')
    .toString().split('\0').filter(Boolean);
  if (changes.length === 0) {
    core.info('Documentation is already current');
    return;
  }
  const additions = [];
  const deletions = [];
  for (let i = 0; i < changes.length; i += 2) {
    const [status, path] = changes.slice(i, i + 2);
    if (!path?.startsWith('docs/') || !['A', 'M', 'D'].includes(status)) {
      throw new Error('Only generated documentation files may be committed');
    }
    if (status === 'D') {
      deletions.push({ path });
    } else {
      const mode = git('ls-files', '--stage', '--', path).toString().slice(0, 6);
      if (mode !== '100644') {
        throw new Error(`Unsupported documentation file mode: ${mode}`);
      }
      additions.push({ path, contents: git('show', `:${path}`).toString('base64') });
    }
  }
  const tree = git('write-tree').toString().trim();
  const { owner, repo } = context.repo;
  const branch = context.ref.slice('refs/heads/'.length);
  let sha;
  try {
    const result = await github.graphql(MUTATION, {
      input: {
        branch: { repositoryNameWithOwner: `${owner}/${repo}`, refName: branch },
        expectedHeadOid: base,
        message: {
          headline: MESSAGE.split('\n')[0],
          body: MESSAGE.slice(MESSAGE.indexOf('\n') + 2),
        },
        fileChanges: { additions, deletions },
      },
    });
    sha = result.createCommitOnBranch.commit.oid;
  } catch {
    // A lost response may follow a successful commit. Observe before replaying.
    core.info('Commit response unavailable; checking the branch for the exact update');
    const ref = await github.rest.git.getRef({ owner, repo, ref: `heads/${branch}` });
    sha = ref.data.object.sha;
  }
  const { data: commit } = await github.rest.repos.getCommit({ owner, repo, ref: sha });
  if (commit.parents.length !== 1 || commit.parents[0].sha !== base ||
      commit.commit.tree.sha !== tree || commit.commit.message.trimEnd() !== MESSAGE ||
      commit.commit.verification.verified !== true) {
    throw new Error('Could not confirm the exact signed documentation commit; refusing to overwrite the branch');
  }
  core.info(`Created verified documentation commit ${sha}`);
  core.setOutput('commit-sha', sha);
};
