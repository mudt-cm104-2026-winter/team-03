# How we review (DRAFT for TC to rewrite in his own words)

> The course wants this page in your own words with one real example from your PRs.
> Use this outline, then replace every section with what you actually do.

## What a reviewer checks
- Does the PR description say what changed and why, and contain `closes #n`?
- Are the commits small, with clear messages?
- Does the code do what the issue says? Pull the branch and run it.
- Is there one line in `CHANGELOG.md`? No secrets, no real data?

## Comment, Approve or Request changes
- **Comment**: a question or a small remark, nothing blocks the merge.
- **Approve**: it meets the "Done when" list of the issue.
- **Request changes**: a real problem (missing edge case, no test, unclear description). The author fixes it and pushes; the reviewer then approves.

## How to leave a line comment
Open the PR, go to **Files changed**, hover the line, click the blue **+**, write the comment, choose **Start a review**.

## How to resolve a merge conflict
`git switch your-branch`, `git fetch`, `git merge origin/main`, edit the files and keep every line from every person, `git add`, `git commit --no-edit`, `git push`. Do not use "Update branch" or the web editor.

## Real example from our PRs
TODO: link the PR where the Request changes happened and describe what was fixed.
