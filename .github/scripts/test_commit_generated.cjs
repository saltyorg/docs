const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { afterEach, beforeEach, test } = require('node:test');
const commitGenerated = require('./commit_generated.cjs');

let root, previous, checkout, base, github, context, calls;
const sha = 'c'.repeat(40);
const git = (...args) => execFileSync('git', args, { cwd: checkout, stdio: ['ignore', 'pipe', 'pipe'] }).toString().trim();
const core = { info() {}, setOutput() {} };

beforeEach(() => {
  previous = process.cwd();
  root = fs.mkdtempSync(path.join(os.tmpdir(), 'docs-signed-commit-'));
  checkout = path.join(root, 'docs');
  fs.mkdirSync(path.join(checkout, 'docs/apps'), { recursive: true });
  fs.writeFileSync(path.join(checkout, 'docs/apps/old.md'), 'old\n');
  git('init', '--initial-branch=main');
  git('add', '.');
  git('-c', 'user.name=fixture', '-c', 'user.email=fixture@example.invalid',
      '-c', 'commit.gpgsign=false', 'commit', '-m', 'fixture');
  base = git('rev-parse', 'HEAD');
  calls = [];
  context = { ref: 'refs/heads/main', repo: { owner: 'saltyorg', repo: 'docs' } };
  github = {
    graphql: async (query, { input }) => {
      calls.push(input);
      return { createCommitOnBranch: { commit: { oid: sha } } };
    },
    rest: {
      git: { getRef: async () => ({ data: { object: { sha } } }) },
      repos: { getCommit: async () => ({ data: {
        parents: [{ sha: base }],
        commit: {
          tree: { sha: git('write-tree') },
          message: 'docs: automated documentation update\n\nUpdated by sb-docs automation\n\n🤖 Generated with sb-docs',
          verification: { verified: true },
        },
      } }) },
    },
  };
  process.chdir(root);
});

afterEach(() => {
  process.chdir(previous);
  fs.rmSync(root, { recursive: true });
});

test('no changes makes no API call', async () => {
  await commitGenerated({ github, core, context });
  assert.equal(calls.length, 0);
});

test('sends new files and deletions with the checked-out head as the atomic guard', async () => {
  fs.unlinkSync(path.join(checkout, 'docs/apps/old.md'));
  fs.writeFileSync(path.join(checkout, 'docs/apps/new name.md'), 'new content\n');
  fs.writeFileSync(path.join(checkout, 'unrelated.txt'), 'leave out\n');
  await commitGenerated({ github, core, context });
  assert.equal(calls.length, 1);
  assert.equal(calls[0].expectedHeadOid, base);
  assert.deepEqual(calls[0].branch, { repositoryNameWithOwner: 'saltyorg/docs', refName: 'main' });
  assert.deepEqual(calls[0].fileChanges.deletions, [{ path: 'docs/apps/old.md' }]);
  assert.deepEqual(calls[0].fileChanges.additions, [
    { path: 'docs/apps/new name.md', contents: Buffer.from('new content\n').toString('base64') },
  ]);
  assert.equal(git('rev-parse', 'HEAD'), base);
});

test('accepts an exact verified commit after a lost response without replaying the mutation', async () => {
  fs.writeFileSync(path.join(checkout, 'docs/apps/old.md'), 'changed\n');
  github.graphql = async (query, { input }) => { calls.push(input); throw new Error('lost response'); };
  await commitGenerated({ github, core, context });
  assert.equal(calls.length, 1);
});

test('rejects a competing commit after a stale-head error', async () => {
  fs.writeFileSync(path.join(checkout, 'docs/apps/old.md'), 'changed\n');
  github.graphql = async () => { throw new Error('stale head'); };
  const getCommit = github.rest.repos.getCommit;
  github.rest.repos.getCommit = async () => {
    const response = await getCommit();
    response.data.parents[0].sha = 'd'.repeat(40);
    return response;
  };
  await assert.rejects(commitGenerated({ github, core, context }), /exact signed documentation commit/);
});

test('rejects an unverified commit', async () => {
  fs.writeFileSync(path.join(checkout, 'docs/apps/old.md'), 'changed\n');
  const getCommit = github.rest.repos.getCommit;
  github.rest.repos.getCommit = async () => {
    const response = await getCommit();
    response.data.commit.verification.verified = false;
    return response;
  };
  await assert.rejects(commitGenerated({ github, core, context }), /exact signed documentation commit/);
});

test('rejects executable files before contacting GitHub', async () => {
  fs.chmodSync(path.join(checkout, 'docs/apps/old.md'), 0o755);
  await assert.rejects(commitGenerated({ github, core, context }), /Unsupported documentation file mode/);
  assert.equal(calls.length, 0);
});

test('rejects unrelated staged files before contacting GitHub', async () => {
  fs.writeFileSync(path.join(checkout, 'unrelated.txt'), 'leave out\n');
  git('add', 'unrelated.txt');
  await assert.rejects(commitGenerated({ github, core, context }), /Only generated documentation/);
  assert.equal(calls.length, 0);
});
