# Mini SIEM - team plan (Assessment 1, stage 1)

**Deadline:** Thursday 19.11.2026, 13:00. Tag `stage-1` must be on GitHub.
**Team:** Person A, Person B, Person C (replace with real names).
**Grade focus:** how you work with Git and GitHub, not how much the app can do.

## The idea in one sentence

A small Python web app where you paste fake log lines; the app stores them and shows
event counts, the top source IPs, and an alert for repeated failed logins.

Fake data only: IPs from `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`.
No real logs, no secrets, no personal data (the repo is public).

## Before anyone codes

Person A reads the existing "Things to bring" app (file names, how it runs) and writes
the layout into Epic 1. The names below are suggestions: adapt them to the existing app.

Log line:
```
2026-11-09 10:15:02 192.0.2.10 FAILED_LOGIN admin
```
One parsed entry: `{"timestamp": ..., "ip": ..., "event": ..., "user": ...}`

Suggested functions: `parse_line(line)`, `save_entries(entries)`, `get_entries()`,
`count_by_event(entries)`, `top_ips(entries, n=5)`, `find_alerts(entries, threshold=3)`.

## Board

In repository `team-NN` -> tab **Projects** -> **New project** -> **Start from scratch** -> **Board**.
(Not under your profile picture.) Columns: Todo, In Progress, Done.
Three epics (issues with the label `epic`), the other issues are their sub-issues.

## Who does what

| Epic | Issue | Owner | Branch | Kind |
|---|---|---|---|---|
| 1 Log input and storage | Log form replaces the example form | A | `feature/log-form` | code |
| | Parse a log line | B | `feature/parser` | code |
| | Store and load entries | B | `feature/storage` | code |
| 2 Analysis and alerts | Sample log file with fake data | C | `feature/sample-logs` | data |
| | Count events by type | C | `feature/count-events` | code |
| | Top source IPs | A | `feature/top-ips` | code |
| | Alert on repeated failed logins | C | `feature/alerts` | code |
| 3 Docs and team process | README sections and CHANGELOG | A | `docs/readme` | docs |
| | `docs/how-we-review.md` | B | `docs/how-we-review` | docs |
| | `docs/glossary.md` (SIEM terms) | C | `docs/glossary` | docs |

Every person has at least 3 PRs (minimum required: 2), and every person has code
and documentation.

| Person | PRs |
|---|---|
| A | log form, top IPs, README + CHANGELOG |
| B | parser, storage, how-we-review |
| C | sample logs, count events, alerts, glossary |

## Reviews (everyone reviews, everyone gets reviewed)

| | Round 1 (first PR of each person) | Round 2 (later PRs) |
|---|---|---|
| A is reviewed by | C | B |
| B is reviewed by | A | C |
| C is reviewed by | B | A |

Every review has at least one comment on a specific line.

## Required moments (plan them, don't hope for them)

- **Conflict:** each person adds their own line under `## Team` in `README.md` and one line to
  `CHANGELOG.md` in their first PR. The second and third PR to be merged will conflict.
  Solve it on your laptop: `git switch your-branch`, `git fetch`, `git merge origin/main`,
  fix the files, `git add`, `git commit`, `git push`. The result is visible in the PR.
- **Request changes:** the reviewer of the first PR of B (A) uses "Request changes" if they find a real
  point (missing edge case, unclear commit message, missing PR description, no test). The author fixes
  it in new commits and the reviewer approves afterwards.
- **Readable history:** commit messages like "Add parse_line for auth log format",
  never "fix", "asdf", "final2".

## Timeline

| When | What |
|---|---|
| Mon 9.11. - Wed 11.11. | Board and 3 epics in the repo, all issues created and assigned, A writes the layout into Epic 1 |
| Thu 12.11. - Sat 14.11. | First PRs from everyone, round 1 reviews, conflict and Request changes happen |
| Mon 16.11. | Interim status from the course: compare it with the checklist below |
| Mon 16.11. - Tue 17.11. | Round 2 PRs and reviews, docs finished |
| Wed 18.11. | Check everything together on github.com, one person sets the tag `stage-1` |
| Thu 19.11., 13:00 | Deadline |

## Checklist (tick together on Wed 18.11.)

Team
- [ ] No direct commits on `main` (all changes through PRs)
- [ ] Every PR closes its issue with `closes #n`
- [ ] Board in the repo (visible under Projects), 3 epics with sub-issues, cards in the right columns
- [ ] At least one resolved conflict, visible in a PR
- [ ] At least one review with Request changes, fixed by the author
- [ ] Readable commit history
- [ ] README has: What this is, How to run it, Team, How we work, Sources, Use of AI
- [ ] Tag `stage-1` is listed under Tags on github.com

Per person (A / B / C)
- [ ] At least 2 own PRs merged, each with a description (what and why)
- [ ] At least 1 review of someone else's PR with a comment on a line

## About AI

Planning help from Claude (project idea, task split, drafts of these files) goes into
`## Use of AI` with date, tool, what for, and how you checked it. Write your own code
in small commits and be ready to explain every line.
