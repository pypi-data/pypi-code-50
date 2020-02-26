#!/usr/bin/env python3

import re
import ghstack
import ghstack.git
import ghstack.shell
import ghstack.github
import ghstack.logging
from ghstack.typing import GitHubNumber, GitHubRepositoryId, GhNumber, GitCommitHash, GitTreeHash
from typing import List, Optional, NamedTuple, Tuple, Set
import logging
from dataclasses import dataclass

# Either "base", "head" or "orig"; which of the ghstack generated
# branches this diff corresponds to
BranchKind = str

# Metadata describing a diff we submitted to GitHub
# TODO: Make this directly contain a DiffWithGitHubMetadata?
DiffMeta = NamedTuple('DiffMeta', [
    ('title', str),
    ('number', GitHubNumber),
    ('body', str),
    ('ghnum', GhNumber),
    # What Git commit hash we should push to what branch
    ('push_branches', Tuple[Tuple[GitCommitHash, BranchKind], ...]),
    # What Git commit hash corresponds to head for this
    # (previously, we got this out of push_branches, but this is not
    # guaranteed to be set.)  None if we didn't change it.
    ('head_branch', Optional[GitCommitHash]),
    # A human-readable string like 'Created' which describes what
    # happened to this pull request
    ('what', str),
    ('closed', bool),
    ('pr_url', str),
])


# Ya, sometimes we get carriage returns.  Crazy right?
RE_STACK = re.compile(r'Stack.*:\r?\n(\* [^\r\n]+\r?\n)+')


# NB: This regex is fuzzy because the D1234567 identifier is typically
# linkified.
RE_DIFF_REV = re.compile(r'^Differential Revision:.+?(D[0-9]+)', re.MULTILINE)


# Suppose that you have submitted a commit to GitHub, and that commit's
# tree was AAA.  The ghstack-source-id of your local commit after this
# submit is AAA.  When you submit a new change on top of this, we check
# that the source id associated with your orig commit agrees with what's
# recorded in GitHub: this lets us know that you are "up-to-date" with
# what was stored on GitHub.  Then, we update the commit message on your
# local commit to record a new ghstack-source-id and push it to orig.
#
# We must store this in the orig commit as we have no other mechanism of
# attaching information to a commit in question.  We don't store this in
# the pull request body as there isn't really any need to do so.
RE_GHSTACK_SOURCE_ID = re.compile(r'^ghstack-source-id: (.+)\n?', re.MULTILINE)


# repo layout:
#   - gh/username/23/base -- what we think GitHub's current tip for commit is
#   - gh/username/23/head -- what we think base commit for commit is
#   - gh/username/23/orig -- the "clean" commit history, i.e., what we're
#                      rebasing, what you'd like to cherry-pick (???)
#                      (Maybe this isn't necessary, because you can
#                      get the "whole" diff from GitHub?  What about
#                      commit description?)


def branch(username: str, ghnum: GhNumber, kind: BranchKind
           ) -> GitCommitHash:
    return GitCommitHash("gh/{}/{}/{}".format(username, ghnum, kind))


def branch_base(username: str, ghnum: GhNumber) -> GitCommitHash:
    return branch(username, ghnum, "base")


def branch_head(username: str, ghnum: GhNumber) -> GitCommitHash:
    return branch(username, ghnum, "head")


def branch_orig(username: str, ghnum: GhNumber) -> GitCommitHash:
    return branch(username, ghnum, "orig")


STACK_HEADER = "Stack from [ghstack](https://{github_url}/ezyang/ghstack)"


@dataclass
class DiffWithGitHubMetadata:
    diff: ghstack.diff.Diff
    number: GitHubNumber
    # Really ought not to be optional, but for BC reasons it might be
    remote_source_id: Optional[str]
    title: str
    body: str
    closed: bool
    ghnum: GhNumber
    pull_request_resolved: ghstack.diff.PullRequestResolved


def main(msg: Optional[str],
         username: str,
         github: ghstack.github.GitHubEndpoint,
         update_fields: bool = False,
         sh: Optional[ghstack.shell.Shell] = None,
         stack_header: str = STACK_HEADER,
         repo_owner: Optional[str] = None,
         repo_name: Optional[str] = None,
         short: bool = False,
         force: bool = False,
         no_skip: bool = False,
         github_url: str = "github.com",
         ) -> List[DiffMeta]:

    if sh is None:
        # Use CWD
        sh = ghstack.shell.Shell()

    if repo_owner is None or repo_name is None:
        # Grovel in remotes to figure it out
        origin_url = sh.git("remote", "get-url", "origin")
        while True:
            match = r'^git@{github_url}:([^/]+)/([^.]+)(?:\.git)?$'.format(
                github_url=github_url
            )
            m = re.match(match, origin_url)
            if m:
                repo_owner_nonopt = m.group(1)
                repo_name_nonopt = m.group(2)
                break
            search = r'{github_url}/([^/]+)/([^.]+)'.format(
                github_url=github_url
            )
            m = re.search(search, origin_url)
            if m:
                repo_owner_nonopt = m.group(1)
                repo_name_nonopt = m.group(2)
                break
            raise RuntimeError(
                "Couldn't determine repo owner and name from url: {}"
                .format(origin_url))
    else:
        repo_owner_nonopt = repo_owner
        repo_name_nonopt = repo_name

    # TODO: Cache this guy
    repo = github.graphql(
        """
        query ($owner: String!, $name: String!) {
            repository(name: $name, owner: $owner) {
                id
                isFork
            }
        }""",
        owner=repo_owner_nonopt,
        name=repo_name_nonopt)["data"]["repository"]

    if repo["isFork"]:
        raise RuntimeError(
            "Cowardly refusing to upload diffs to a repository that is a "
            "fork.  ghstack expects 'origin' of your Git checkout to point "
            "to the upstream repository in question.  If your checkout does "
            "not comply, please adjust your remotes (by editing .git/config) "
            "to make it so.  If this message is in error, please register "
            "your complaint on GitHub issues (or edit this line to delete "
            "the check above.")
    repo_id = repo["id"]

    sh.git("fetch", "origin")
    base = GitCommitHash(sh.git("merge-base", "origin/master", "HEAD"))

    # compute the stack of commits to process (reverse chronological order),
    stack = ghstack.git.parse_header(
        sh.git("rev-list", "--header", "^" + base, "HEAD"),
        github_url,
    )

    # compute the base commit
    base_obj = ghstack.git.split_header(sh.git("rev-list", "--header", "^" + base + "^@", base))[0]

    assert len(stack) > 0

    ghstack.logging.record_status(
        "{} \"{}\"".format(stack[0].oid[:9], stack[0].title))

    submitter = Submitter(github=github,
                          sh=sh,
                          username=username,
                          repo_owner=repo_owner_nonopt,
                          repo_name=repo_name_nonopt,
                          repo_id=repo_id,
                          base_commit=base,
                          base_tree=base_obj.tree(),
                          stack_header=stack_header,
                          update_fields=update_fields,
                          msg=msg,
                          short=short,
                          force=force,
                          no_skip=no_skip,
                          stack=list(reversed(stack)),
                          github_url=github_url)
    submitter.prepare_updates()
    submitter.push_updates()

    # NB: earliest first
    return submitter.stack_meta


def all_branches(username: str, ghnum: GhNumber) -> Tuple[str, str, str]:
    return (branch_base(username, ghnum),
            branch_head(username, ghnum),
            branch_orig(username, ghnum))


def push_spec(commit: GitCommitHash, branch: str) -> str:
    return "{}:refs/heads/{}".format(commit, branch)


class Submitter(object):
    """
    A class responsible for managing all of the environment and mutable
    state associated with submitting PRs to GitHub.

    Standard usage is::

        submitter.prepare_updates()  # populates stack_meta, creates new PRs
        submitter.push_updates()

    This is split up in a weird way because some users of this class
    need to interpose between the initial preparation of updates,
    and when we actually push the updates.

    NB: prepare_updates() will push updates to GitHub in order to get
    GitHub PR numbers for other usage.
    """

    # Endpoint to access GitHub
    github: ghstack.github.GitHubEndpoint

    # Shell inside git checkout that we are submitting
    sh: ghstack.shell.Shell

    # GitHub username who is doing the submitting
    username: str

    # Owner of the repository we are submitting to.  Usually 'pytorch'
    repo_owner: str

    # Name of the repository we are submitting to.  Usually 'pytorch'
    repo_name: str

    # GraphQL ID of the repository
    repo_id: GitHubRepositoryId

    # The base commit of the prev diff we submitted.  This
    # corresponds to the 'head' branch in GH.
    # INVARIANT: This is REALLY a hash, and not some random ref!
    base_commit: GitCommitHash

    # The base tree of the prev diff we submitted.
    # INVARIANT: This is base_commit^{tree}!  Cached here so we
    # don't have to keep asking about it.
    base_tree: GitTreeHash

    # The orig commit of the prev diff we submitted.  This
    # corresponds to the 'orig' branch in GH.
    base_orig: GitCommitHash

    # Message describing the update to the stack that was done
    msg: Optional[str]

    # Description of all the diffs we submitted; to be populated
    # by Submitter.
    stack_meta: List[DiffMeta]

    # List of input diffs which we ignored (i.e., treated as if they
    # did not exist on the stack at all), because they were associated
    # with a patch that contains no changes.  GhNumber may be false
    # if the diff was never associated with a PR.
    ignored_diffs: List[Tuple[ghstack.diff.Diff, Optional[GitHubNumber]]]

    # List of diffs to process, in chronological order
    stack: List[ghstack.diff.Diff]

    # Set of seen ghnums
    seen_ghnums: Set[GhNumber]

    # String used to describe the stack in question
    stack_header: str

    # Clobber existing PR description with local commit message
    update_fields: bool

    # Print only PR URL to stdout
    short: bool

    # Force an update to GitHub, even if we think that your local copy
    # is stale.
    force: bool

    # Do not skip unchanged diffs
    no_skip: bool

    # Github url (normally github.com)
    github_url: str

    def __init__(
            self,
            github: ghstack.github.GitHubEndpoint,
            sh: ghstack.shell.Shell,
            username: str,
            repo_owner: str,
            repo_name: str,
            repo_id: GitHubRepositoryId,
            base_commit: GitCommitHash,
            base_tree: GitTreeHash,
            stack_header: str,
            update_fields: bool,
            msg: Optional[str],
            stack: List[ghstack.diff.Diff],
            short: bool,
            force: bool,
            no_skip: bool,
            github_url: str,):
        self.github = github
        self.sh = sh
        self.username = username
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.repo_id = repo_id
        self.base_commit = base_commit
        self.base_orig = base_commit
        self.base_tree = base_tree
        self.update_fields = update_fields
        self.stack_header = None if stack_header is None else stack_header.format(github_url=github_url)
        self.stack_meta = []
        self.ignored_diffs = []
        self.stack = stack
        self.seen_ghnums = set()
        self.msg = msg
        self.short = short
        self.force = force
        self.no_skip = no_skip
        self.github_url = github_url

    def _default_title_and_body(self, commit: ghstack.diff.Diff,
                                old_pr_body: Optional[str]
                                ) -> Tuple[str, str]:
        """
        Compute what the default title and body of a newly opened pull
        request would be, given the existing commit message.

        If you pass in the old PR body, we also preserve "Differential
        Revision" information in the PR body.  We only overwrite PR
        body if you explicitly ask for it with --update-fields, but
        it's good not to lose Phabricator diff assignment, so we special
        case this.
        """
        title = commit.title
        extra = ''
        if old_pr_body is not None:
            # Look for tags we should preserve, and keep them
            m = RE_DIFF_REV.search(old_pr_body)
            if m:
                extra = (
                    "\n\nDifferential Revision: "
                    "[{phabdiff}]"
                    "(https://our.internmc.facebook.com/intern/diff/{phabdiff})"
                ).format(phabdiff=m.group(1))
        commit_body = ''.join(commit.summary.splitlines(True)[1:]).lstrip()
        # Don't store ghstack-source-id in the PR body; it will become
        # stale quickly
        commit_body = RE_GHSTACK_SOURCE_ID.sub('', commit_body)
        # Don't store Pull request resolved in the PR body; it's
        # unnecessary
        commit_body = ghstack.diff.re_pull_request_resolved_w_sp(self.github_url).sub('', commit_body)
        pr_body = (
            "{}:\n* (to be filled)\n\n{}{}"
            .format(self.stack_header,
                    commit_body,
                    extra)
        )
        return title, pr_body

    def elaborate_diff(self, commit: ghstack.diff.Diff, *,
                       is_ghexport: bool = False) -> DiffWithGitHubMetadata:
        """
        Query GitHub API for the current title, body and closed? status
        of the pull request corresponding to a ghstack.diff.Diff.
        """

        assert commit.pull_request_resolved is not None
        assert commit.pull_request_resolved.owner == self.repo_owner
        assert commit.pull_request_resolved.repo == self.repo_name

        number = commit.pull_request_resolved.number
        # TODO: There is no reason to do a node query here; we can
        # just look up the repo the old fashioned way
        r = self.github.graphql("""
          query ($repo_id: ID!, $number: Int!) {
            node(id: $repo_id) {
              ... on Repository {
                pullRequest(number: $number) {
                  body
                  title
                  closed
                  headRefName
                }
              }
            }
          }
        """, repo_id=self.repo_id, number=number)["data"]["node"]["pullRequest"]

        # Sorry, this is a big hack to support the ghexport case
        m = re.match(r'(refs/heads/)?export-D([0-9]+)$', r['headRefName'])
        if m is not None and is_ghexport:
            raise RuntimeError('''\
This commit appears to already be associated with a pull request,
but the pull request was previously submitted with an old version of
ghexport.  You can continue exporting using the old style using:

    ghexport --legacy

For future diffs, we recommend using the non-legacy version of ghexport
as it supports bidirectional syncing.  However, there is no way to
convert a pre-existing PR in the old style to the new format which
supports bidirectional syncing.  If you would like to blow away the old
PR and start anew, edit the Summary in the Phabricator diff to delete
the line 'Pull Request resolved' and then run ghexport again.
''')

        # TODO: Hmm, I'm not sure why this matches
        m = re.match(r'gh/[^/]+/([0-9]+)/head$', r['headRefName'])
        if m is None:
            if is_ghexport:
                raise RuntimeError('''\
This commit appears to already be associated with a pull request,
but the pull request doesn't look like it was submitted by ghexport
Maybe you exported it using the "Export to Open Source" button on
the Phabricator diff page?  If so, please continue to use that button
to export your diff.

If you think this is in error, edit the Summary in the Phabricator diff
to delete the line 'Pull Request resolved' and then run ghexport again.
''')
            else:
                raise RuntimeError('''\
This commit appears to already be associated with a pull request,
but the pull request doesn't look like it was submitted by ghstack.
If you think this is in error, run:

    ghstack unlink {}

to disassociate the commit with the pull request, and then try again.
(This will create a new pull request!)
'''.format(commit.oid))
        gh_number = GhNumber(m.group(1))

        # NB: Technically, we don't need to pull this information at
        # all, but it's more convenient to unconditionally edit
        # title/body when we update the pull request info
        title = r['title']
        pr_body = r['body']
        if self.update_fields:
            title, pr_body = self._default_title_and_body(commit, pr_body)

        # TODO: remote summary should be done earlier so we can use
        # it to test if updates are necessary
        remote_summary = ghstack.git.split_header(
            self.sh.git(
                "rev-list", "--max-count=1", "--header", "origin/" + branch_orig(self.username, gh_number)
            )
        )[0]
        m_remote_source_id = RE_GHSTACK_SOURCE_ID.search(remote_summary.commit_msg())
        remote_source_id = m_remote_source_id.group(1) if m_remote_source_id else None

        return DiffWithGitHubMetadata(
            diff=commit,
            title=title,
            body=pr_body,
            closed=r['closed'],
            number=number,
            ghnum=gh_number,
            remote_source_id=remote_source_id,
            pull_request_resolved=commit.pull_request_resolved,
        )

    def skip_commit(self, commit: DiffWithGitHubMetadata) -> None:
        """
        Skip a diff, because we happen to know that there were no local
        changes.  We have to update the internal metadata of the Submitter,
        so you're still obligated to call this even if you think there's
        nothing to do.
        """

        ghnum = commit.ghnum

        self.stack_meta.append(DiffMeta(
            title=commit.title,
            number=commit.number,
            body=commit.body,
            ghnum=ghnum,
            push_branches=(),
            head_branch=None,
            what='Skipped',
            closed=commit.closed,
            pr_url=commit.pull_request_resolved.url(self.github_url),
        ))

        self.base_commit = GitCommitHash(self.sh.git(
            "rev-parse", "origin/" + branch_head(self.username, ghnum)))
        self.base_orig = GitCommitHash(self.sh.git(
            "rev-parse", "origin/" + branch_orig(self.username, ghnum)
        ))
        self.base_tree = GitTreeHash(self.sh.git(
            "rev-parse", self.base_orig + "^{tree}"
        ))

    def process_new_commit(self, commit: ghstack.diff.Diff) -> None:
        """
        Process a diff that has never been pushed to GitHub before.
        """

        if '[ghstack-poisoned]' in commit.summary:
            raise RuntimeError('''\
This commit is poisoned: it is from a head or base branch--ghstack
cannot validly submit it.  The most common situation for this to
happen is if you checked out the head branch of a pull request that was
previously submitted with ghstack (e.g., by using hub checkout).
Making modifications on the head branch is not supported; instead,
you should fetch the original commits in question by running:

    ghstack checkout $PR_URL

Since we cannot proceed, ghstack will abort now.
''')

        title, pr_body = self._default_title_and_body(commit, None)

        # Determine the next available GhNumber.  We do this by
        # iterating through known branches and keeping track
        # of the max.  The next available GhNumber is the next number.
        # This is technically subject to a race, but we assume
        # end user is not running this script concurrently on
        # multiple machines (you bad bad)
        refs = self.sh.git(
            "for-each-ref",
            "refs/remotes/origin/gh/{}".format(self.username),
            "--format=%(refname)").split()
        max_ref_num = max(int(ref.split('/')[-2]) for ref in refs) \
            if refs else 0
        ghnum = GhNumber(str(max_ref_num + 1))

        # Create the incremental pull request diff
        tree = commit.patch.apply(self.sh, self.base_tree)

        # Actually, if there's no change in the tree, stop processing
        if tree == self.base_tree:
            self.ignored_diffs.append((commit, None))
            logging.warn("Skipping {} {}, as the commit has no changes"
                         .format(commit.oid, title))
            return

        assert ghnum not in self.seen_ghnums
        self.seen_ghnums.add(ghnum)

        new_pull = GitCommitHash(
            self.sh.git("commit-tree", tree,
                        "-p", self.base_commit,
                        input=commit.summary + "\n\n[ghstack-poisoned]"))

        # Push the branches, so that we can create a PR for them
        new_branches = (
            push_spec(new_pull, branch_head(self.username, ghnum)),
            push_spec(self.base_commit, branch_base(self.username, ghnum))
        )
        self.sh.git(
            "push",
            "origin",
            *new_branches,
        )
        self.github.push_hook(new_branches)

        # Time to open the PR
        # NB: GraphQL API does not support opening PRs
        r = self.github.post(
            "repos/{owner}/{repo}/pulls"
            .format(owner=self.repo_owner, repo=self.repo_name),
            title=title,
            head=branch_head(self.username, ghnum),
            base=branch_base(self.username, ghnum),
            body=pr_body,
            maintainer_can_modify=True,
        )
        number = r['number']

        logging.info("Opened PR #{}".format(number))

        # Update the commit message of the local diff with metadata
        # so we can correlate these later
        pull_request_resolved = ghstack.diff.PullRequestResolved(
            owner=self.repo_owner, repo=self.repo_name, number=number)
        commit_msg = ("{commit_msg}\n\n"
                      "ghstack-source-id: {sourceid}\n"
                      "Pull Request resolved: "
                      "https://{github_url}/{owner}/{repo}/pull/{number}"
                      .format(commit_msg=commit.summary.rstrip(),
                              owner=self.repo_owner,
                              repo=self.repo_name,
                              number=number,
                              sourceid=commit.source_id,
                              github_url=self.github_url))

        # TODO: Try harder to preserve the old author/commit
        # information (is it really necessary? Check what
        # --amend does...)
        new_orig = GitCommitHash(self.sh.git(
            "commit-tree",
            tree,
            "-p", self.base_orig,
            input=commit_msg))

        self.stack_meta.append(DiffMeta(
            title=title,
            number=number,
            body=pr_body,
            ghnum=ghnum,
            push_branches=((new_orig, 'orig'), ),
            head_branch=new_pull,
            what='Created',
            closed=False,
            pr_url=pull_request_resolved.url(self.github_url),
        ))

        self.base_commit = new_pull
        self.base_orig = new_orig
        self.base_tree = tree

    def process_old_commit(self, elab_commit: DiffWithGitHubMetadata) -> None:
        """
        Process a diff that has an existing upload to GitHub.
        """

        commit = elab_commit.diff
        ghnum = elab_commit.ghnum
        number = elab_commit.number

        if ghnum in self.seen_ghnums:
            raise RuntimeError(
                "Something very strange has happened: a commit for "
                "the pull request #{} occurs twice in your local "
                "commit stack.  This is usually because of a botched "
                "rebase.  Please take a look at your git log and seek "
                "help from your local Git expert.".format(number))
        self.seen_ghnums.add(ghnum)

        logging.info("Pushing to #{}".format(number))

        # Compute the local and remote source IDs
        summary = commit.summary
        m_local_source_id = RE_GHSTACK_SOURCE_ID.search(summary)
        if m_local_source_id is None:
            # For BC, just slap on a source ID.  After BC is no longer
            # needed, we can just error in this case; however, this
            # situation is extremely likely to happen for preexisting
            # stacks.
            logging.warning(
                "Local commit has no ghstack-source-id; assuming that it is "
                "up-to-date with remote.")
            summary = "{}\nghstack-source-id: {}".format(summary, commit.source_id)
        else:
            local_source_id = m_local_source_id.group(1)
            if elab_commit.remote_source_id is None:
                # This should also be an error condition, but I suppose
                # it can happen in the wild if a user had an aborted
                # ghstack run, where they updated their head pointer to
                # a copy with source IDs, but then we failed to push to
                # orig.  We should just go ahead and push in that case.
                logging.warning(
                    "Remote commit has no ghstack-source-id; assuming that we are "
                    "up-to-date with remote.")
            else:
                if local_source_id != elab_commit.remote_source_id and not self.force:
                    raise RuntimeError(
                        "Cowardly refusing to push an update to GitHub, since it "
                        "looks another source has updated GitHub since you last "
                        "pushed.  If you want to push anyway, rerun this command "
                        "with --force.  Otherwise, diff your changes against "
                        "{} and reapply them on top of an up-to-date commit from "
                        "GitHub.".format(local_source_id))
                summary = RE_GHSTACK_SOURCE_ID.sub(
                    'ghstack-source-id: {}\n'.format(commit.source_id),
                    summary)

        # We've got an update to do!  But what exactly should we
        # do?
        #
        # Here are a number of situations which may have
        # occurred.
        #
        #   1. None of the parent commits changed, and this is
        #      the first change we need to push an update to.
        #
        #   2. A parent commit changed, so we need to restack
        #      this commit too.  (You can't easily tell distinguish
        #      between rebase versus rebase+amend)
        #
        #   3. The parent is now master (any prior parent
        #      commits were absorbed into master.)
        #
        #   4. The parent is totally disconnected, the history
        #      is bogus but at least the merge-base on master
        #      is the same or later.  (This can occur if you
        #      cherry-picked a commit out of an old stack and
        #      want to make it independent.)
        #
        # In cases 1-3, we can maintain a clean merge history
        # if we do a little extra book-keeping, which is what
        # we do now.
        #
        # TODO: What we have here actually works pretty hard to
        # maintain a consistent merge history between all PRs;
        # so, e.g., you could merge with master and things
        # wouldn't break.  But we don't necessarily have to do
        # this; all we need is the delta between base and head
        # to make sense.  The benefit to doing this is you could
        # more easily update single revs only, without doing
        # the rest of the stack.  The downside is that you
        # get less accurate merge structure for your changes
        # (because each "diff" is completely disconnected.)
        #

        # First, check if the parent commit hasn't changed.
        # We do this by checking if our base_commit is the same
        # as the gh/ezyang/X/base commit.
        #
        # In this case, we don't need to include the base as a
        # parent at all; just construct our new diff as a plain,
        # non-merge commit.
        base_args: Tuple[str, ...]
        orig_base_hash = self.sh.git(
            "rev-parse", "origin/" + branch_base(self.username, ghnum))

        # I vacillated between whether or not we should use the PR
        # body or the literal commit message here.  Right now we use
        # the PR body, because after initial commit the original
        # commit message is not supposed to "matter" anymore.  orig
        # still uses the original commit message, however, because
        # it's supposed to be the "original".
        non_orig_commit_msg = RE_STACK.sub('', elab_commit.body)

        if orig_base_hash == self.base_commit:

            new_base = self.base_commit
            base_args = ()

        else:
            # Second, check if our local base (self.base_commit)
            # added some new commits, but is still rooted on the
            # old base.
            #
            # If so, all we need to do is include the local base
            # as a parent when we do the merge.
            is_ancestor = self.sh.git(
                "merge-base",
                "--is-ancestor",
                "origin/" + branch_base(self.username, ghnum),
                self.base_commit, exitcode=True)

            if is_ancestor:
                new_base = self.base_commit

            else:
                # If we've gotten here, it means that the new
                # base and the old base are completely
                # unrelated.  We'll make a fake commit that
                # "resets" the tree back to something that makes
                # sense and merge with that.  This doesn't fix
                # the fact that we still incorrectly report
                # the old base as an ancestor of our commit, but
                # it's better than nothing.
                new_base = GitCommitHash(self.sh.git(
                    "commit-tree", self.base_tree,
                    "-p", "origin/" + branch_base(self.username, ghnum),
                    "-p", self.base_commit,
                    input='Update base for {} on "{}"\n\n{}\n\n[ghstack-poisoned]'
                          .format(self.msg, elab_commit.title,
                                  non_orig_commit_msg)))

            base_args = ("-p", new_base)

        # Blast our current tree as the newest commit, merging
        # against the previous pull entry, and the newest base.

        tree = commit.patch.apply(self.sh, self.base_tree)

        # Nothing to do, just ignore the diff
        if tree == self.base_tree:
            self.ignored_diffs.append((commit, number))
            logging.warn("Skipping PR #{} {}, as the commit now has no changes"
                         .format(number, elab_commit.title))
            return

        new_pull = GitCommitHash(self.sh.git(
            "commit-tree", tree,
            "-p", "origin/" + branch_head(self.username, ghnum),
            *base_args,
            input='{} on "{}"\n\n{}\n\n[ghstack-poisoned]'.format(self.msg, elab_commit.title, non_orig_commit_msg)))

        # Perform what is effectively an interactive rebase
        # on the orig branch.
        #
        # Hypothetically, there could be a case when this isn't
        # necessary, but it's INCREDIBLY unlikely (because we'd
        # have to look EXACTLY like the original orig, and since
        # we're in the branch that says "hey we changed
        # something" that's probably not what happened.

        logging.info("Restacking commit on {}".format(self.base_orig))
        new_orig = GitCommitHash(self.sh.git(
            "commit-tree", tree,
            "-p", self.base_orig, input=summary))

        push_branches = (
            (new_base, "base"),
            (new_pull, "head"),
            (new_orig, "orig"),
        )

        if elab_commit.closed:
            what = 'Skipped closed'
        else:
            what = 'Updated'

        self.stack_meta.append(DiffMeta(
            title=elab_commit.title,
            number=number,
            # NB: Ignore the commit message, and just reuse the old commit
            # message.  This is consistent with 'jf submit' default
            # behavior.  The idea is that people may have edited the
            # PR description on GitHub and you don't want to clobber
            # it.
            body=elab_commit.body,
            ghnum=ghnum,
            push_branches=push_branches,
            head_branch=new_pull,
            what=what,
            closed=elab_commit.closed,
            pr_url=elab_commit.pull_request_resolved.url(self.github_url),
        ))

        self.base_commit = new_pull
        self.base_orig = new_orig
        self.base_tree = tree

    def _format_stack(self, index: int) -> str:
        rows = []
        for i, s in reversed(list(enumerate(self.stack_meta))):
            if index == i:
                rows.append('* **#{} {}**'.format(s.number, s.title.strip()))
            else:
                rows.append('* #{} {}'.format(s.number, s.title.strip()))
        return self.stack_header + ':\n' + '\n'.join(rows) + '\n'

    def prepare_updates(self, *, is_ghexport: bool = False) -> None:
        """
        Go through each commit in the stack and construct the commits
        which we will push to GitHub shortly.  If a commit does not have
        an associated PR, push it immediately and create a PR so that we
        ensure that every diff in stack_meta has an associated pull
        request.
        """

        # start with the earliest commit
        skip = True
        for s in self.stack:
            if s.pull_request_resolved is not None:
                d = self.elaborate_diff(s, is_ghexport=is_ghexport)
                # In principle, we can still skip commits if both their
                # trees and orig commits match; and even if the messages
                # don't match we only really need to push an updated
                # orig commit.  However, the code to make this happen is
                # a bit bothersome, so I don't do it for now, to fix a
                # very real bug.
                if skip and d.remote_source_id == s.source_id and not self.no_skip and not self.update_fields:
                    self.skip_commit(d)
                else:
                    skip = False
                    self.process_old_commit(d)
            else:
                skip = False
                self.process_new_commit(s)

    def push_updates(self, *, import_help: bool = True) -> None:  # noqa: C901
        """
        To be called after prepare_updates: actually push the updates to
        GitHub, and also update other metadata in GitHub as necessary.
        Also update the local Git checkout to point to the rewritten commit
        stack.
        """

        # fix the HEAD pointer
        self.sh.git("reset", "--soft", self.base_orig)

        # update pull request information, update bases as necessary
        #   preferably do this in one network call
        # push your commits (be sure to do this AFTER you update bases)
        base_push_branches: List[str] = []
        push_branches: List[str] = []
        force_push_branches: List[str] = []
        for i, s in enumerate(self.stack_meta):
            # NB: GraphQL API does not support modifying PRs
            if not s.closed:
                logging.info(
                    "# Updating https://{github_url}/{owner}/{repo}/pull/{number}"
                    .format(github_url=self.github_url,
                            owner=self.repo_owner,
                            repo=self.repo_name,
                            number=s.number))
                self.github.patch(
                    "repos/{owner}/{repo}/pulls/{number}"
                    .format(owner=self.repo_owner, repo=self.repo_name,
                            number=s.number),
                    body=RE_STACK.sub(self._format_stack(i), s.body),
                    title=s.title)
            else:
                logging.info(
                    "# Skipping closed https://{github_url}/{owner}/{repo}/pull/{number}"
                    .format(github_url=self.github_url,
                            owner=self.repo_owner,
                            repo=self.repo_name,
                            number=s.number))

            # It is VERY important that we do base updates BEFORE real
            # head updates, otherwise GitHub will spuriously think that
            # the user pushed a number of patches as part of the PR,
            # when actually they were just from the (new) upstream
            # branch

            for commit, b in s.push_branches:
                if b == 'orig':
                    q = force_push_branches
                elif b == 'base':
                    q = base_push_branches
                else:
                    q = push_branches
                q.append(push_spec(commit, branch(self.username, s.ghnum, b)))
        # Careful!  Don't push master.
        # TODO: These pushes need to be atomic (somehow)
        if base_push_branches:
            self.sh.git("push", "origin", *base_push_branches)
            self.github.push_hook(base_push_branches)
        if push_branches:
            self.sh.git("push", "origin", *push_branches)
            self.github.push_hook(push_branches)
        if force_push_branches:
            self.sh.git("push", "origin", "--force", *force_push_branches)
            self.github.push_hook(force_push_branches)

        # Report what happened
        def format_url(s: DiffMeta) -> str:
            return ("https://{github_url}/{owner}/{repo}/pull/{number}"
                    .format(github_url=self.github_url,
                            owner=self.repo_owner,
                            repo=self.repo_name,
                            number=s.number))

        if self.short:
            # Guarantee that the FIRST PR URL is the top of the stack
            print('\n'.join(format_url(s) for s in reversed(self.stack_meta)))
            return

        print()
        print('# Summary of changes (ghstack {})'.format(ghstack.__version__))
        print()
        if self.stack_meta:
            for s in reversed(self.stack_meta):
                url = format_url(s)
                print(" - {} {}".format(s.what, url))
            top_of_stack = self.stack_meta[-1]
            print()

            if import_help:
                print("Facebook employees can import your changes by running ")
                print("(on a Facebook machine):")
                print()
                print("    ghimport -s {}".format(format_url(top_of_stack)))
                print()
                print("If you want to work on this diff stack on another machine:")
                print()
                print("    ghstack checkout {}".format(format_url(top_of_stack)))
                print("")
        else:
            print("No pull requests updated; all commits in your diff stack were empty!")

        if self.ignored_diffs:
            print()
            print("FYI: I ignored the following commits, because they had no changes:")
            print()
            noop_pr = False
            for d, pr in reversed(self.ignored_diffs):
                if pr is None:
                    print(" - {} {}".format(d.oid[:8], d.title))
                else:
                    noop_pr = True
                    print(" - {} {} (was previously submitted as PR #{})".format(d.oid[:8], d.title, pr))
            if noop_pr:
                print()
                print("I did NOT close or update PRs previously associated with these commits.")
