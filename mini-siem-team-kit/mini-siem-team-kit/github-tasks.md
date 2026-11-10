# GitHub tasks per person

The code and docs tasks are in `issues.md`. This file covers what each person does
**on GitHub and with Git**, because that is what Assessment 1 looks at.

## Everyone does these (same for A, B and C)

| # | Task | Evidence on github.com |
|---|---|---|
| 1 | Create a branch for your issue (`git switch -c feature/...`) | Branch listed, linked to your PR |
| 2 | Commit in small steps with clear messages | Readable history in your PR |
| 3 | Push and open a PR with a description (what and why) and `closes #n` | PR text, issue closes on merge |
| 4 | Add one line to `CHANGELOG.md` per PR | Line in the diff |
| 5 | Move your own issue cards: Todo -> In Progress -> Done | Board |
| 6 | Review two PRs of teammates, each with at least one comment on a line | Review with line comment |
| 7 | Get your own PR approved and merged (1 approval needed) | Merged PR |
| 8 | After each merge: `git switch main`, `git pull` | Local only, but needed to avoid conflicts |

Minimum from the assignment: 2 own merged PRs and 1 review with a line comment per person.
This plan gives 3 PRs and 2 reviews each.

## One special GitHub job per person

Each person leads one part, so nobody only "writes code".

### Person A: board, epics and the Request changes review
- [ ] Create the board **in the repo** (`team-NN` -> Projects -> New project -> Start from scratch -> Board)
- [ ] Check: the repo's Projects tab lists the board
- [ ] Create the label `epic` and the three epic issues
- [ ] Attach every other issue as a sub-issue of its epic
- [ ] Review the first PR of B and use **Request changes** with a real point and a line comment
- [ ] After B fixes it: re-review and Approve

### Person B: issues, conflict and fixing a review
- [ ] Create all non-epic issues from `issues.md`, with owner (assignee) and branch name in the text
- [ ] Open your first PR early (parser) so it can get the Request changes review
- [ ] Fix the requested changes in new commits and push to the same branch
- [ ] Solve the merge conflict: your first PR is merged **last**, so `main` has moved on
  ```bash
  git switch feature/parser
  git fetch
  git merge origin/main      # conflict in README.md and CHANGELOG.md
  # edit the files, keep every line from every person
  git add README.md CHANGELOG.md
  git commit
  git push
  ```
- [ ] Check in the PR on GitHub that the merge commit and the resolved files are visible

### Person C: final check and the tag
- [ ] Merge your first PR early (sample logs, small) to start the sequence
- [ ] Before the deadline: go through the checklist in `team-plan.md` **on github.com**, not on your laptop
  (PRs, reviews, board columns, README sections, closed issues)
- [ ] Set the tag on the final state of `main`:
  ```bash
  git switch main
  git pull
  git tag stage-1
  git push origin stage-1
  ```
- [ ] Open github.com -> **Tags** and confirm `stage-1` is listed
- [ ] Tell the team the exact commit the tag points to

## Merge order that creates the required conflict

1. C merges `feature/sample-logs` (first PR, small, edits `## Team` and `CHANGELOG.md`)
2. A merges `feature/log-form` (also edits `## Team` and `CHANGELOG.md`)
3. B merges `feature/parser` last: Git reports a conflict, B resolves it on the laptop as above

The Request changes review on B's PR happens before step 3, so B fixes the review and
resolves the conflict in the same PR.

## Evidence summary

| Checklist item | Who | Where to look |
|---|---|---|
| No direct commits on `main` | everyone | Commits on `main` all come from merged PRs |
| Issue per work, `closes #n` | everyone | Closed issues linked to PRs |
| Board with 3 epics in the repo | A | Repo -> Projects |
| Resolved conflict | B | PR with merge commit |
| Request changes, fixed | A (reviewer), B (author) | Review history in B's PR |
| Readable history | everyone | Commit list |
| README sections | A (writes), everyone checks | README on `main` |
| Tag `stage-1` | C | Repo -> Tags |
