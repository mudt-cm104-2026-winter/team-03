# Issues to create (GitHub -> repo team-NN -> Issues -> New issue)

GitHub assigns the numbers. Use them in `closes #n` and for sub-issues.
Create the three epics first (label `epic`), then the other issues and attach them as sub-issues.

**For every issue, the PR must have:** a description (what and why), `closes #n`,
at least 3 small commits with clear messages, one line in `CHANGELOG.md`,
no secrets and no real data.

---

# Epics

## EPIC 1 - Log input and storage
Label: `epic`
Goal: the user can paste fake log lines, the app parses and saves them.
Sub-issues: Log form, Parse a log line, Store and load entries.
Notes (A fills this in): layout of the existing app and the agreed function names.

## EPIC 2 - Analysis and alerts
Label: `epic`
Goal: the app counts events, shows top IPs, and warns about repeated failed logins.
Sub-issues: Sample log file, Count events, Top source IPs, Alert on repeated failed logins.

## EPIC 3 - Docs and team process
Label: `epic`
Goal: README complete, one docs page per person, CHANGELOG kept up to date.
Sub-issues: README and CHANGELOG, How we review, Glossary.

---

# Epic 1: Log input and storage

## Log form replaces the example form  (Person A)
Branch: `feature/log-form`
**What:** Replace the "Things to bring" form with a form where the user pastes log lines (one per line).
Update the page texts so they match the Mini SIEM topic.
**Done when**
- [ ] The page loads and the form sends the pasted text to the app
- [ ] Old example texts are gone or renamed
- [ ] Until parser and storage exist, the app shows a simple "received N lines" message
- [ ] First PR of A: adds one line under `## Team` in `README.md`

## Parse a log line  (Person B)
Branch: `feature/parser`
**What:** Write `parse_line(line)` for `2026-11-09 10:15:02 192.0.2.10 FAILED_LOGIN admin`.
Return a dict with timestamp, ip, event, user. Return `None` for invalid lines
(empty line, too few fields, invalid IP).
**Done when**
- [ ] Valid lines give the right dict, invalid lines give `None` and do not crash
- [ ] At least 3 test lines (valid, empty, broken) are documented in the PR description or in tests
- [ ] First PR of B: adds one line under `## Team` in `README.md`

## Store and load entries  (Person B)
Branch: `feature/storage`
**What:** Save parsed entries in SQLite (`sqlite3`) and load them again. The `.db` file is in `.gitignore`.
**Done when**
- [ ] Entries are still there after restarting the app
- [ ] SQL uses `?` placeholders only, never string formatting (log lines are untrusted input)
- [ ] The form from Person A now saves parsed lines

---

# Epic 2: Analysis and alerts

## Sample log file with fake data  (Person C)
Branch: `feature/sample-logs`
**What:** Create `sample_logs.txt` with about 30 fake lines. Include one clear attack
(one IP with several failed logins) and normal traffic from other IPs.
**Done when**
- [ ] Only documentation IPs (`192.0.2.x`, `198.51.100.x`, `203.0.113.x`) and made-up users
- [ ] At least 3 different event types
- [ ] First PR of C: adds one line under `## Team` in `README.md`

## Count events by type  (Person C)
Branch: `feature/count-events`
**What:** `count_by_event(entries)` returns for example `{"FAILED_LOGIN": 5, "LOGIN_OK": 2}`.
Show the result on the page.
**Done when**
- [ ] Works with an empty list
- [ ] Table visible on the page
- [ ] Checked with `sample_logs.txt`

## Top source IPs  (Person A)
Branch: `feature/top-ips`
**What:** `top_ips(entries, n=5)` returns `[(ip, count), ...]`, highest first. Show it as a table.
**Done when**
- [ ] Sorted from most to fewest, at most n rows
- [ ] Works with an empty list
- [ ] Checked with `sample_logs.txt`

## Alert on repeated failed logins  (Person C)
Branch: `feature/alerts`
**What:** `find_alerts(entries, threshold=3)` returns a message for every IP with at least
`threshold` `FAILED_LOGIN` events, for example `HIGH: 192.0.2.10 had 4 failed logins`.
Show alerts at the top of the page.
**Done when**
- [ ] Sample file triggers at least one alert, normal IPs do not
- [ ] The threshold is a parameter, not a hidden number
- [ ] PR description explains why you chose the default threshold

---

# Epic 3: Docs and team process

## README and CHANGELOG  (Person A)
Branch: `docs/readme`
**What:** Add the six required sections to `README.md` (use `README-template.md`), create `CHANGELOG.md`,
and write `docs/how-to-run.md`.
**Done when**
- [ ] `## What this is`, `## How to run it`, `## Team`, `## How we work`, `## Sources`, `## Use of AI` exist
- [ ] `## Use of AI` lists every use of AI so far, honestly
- [ ] `CHANGELOG.md` has one line per merged PR
- [ ] Someone else ran the app with only your instructions

## How we review  (Person B)
Branch: `docs/how-we-review`
**What:** One page in `docs/how-we-review.md`: what a reviewer checks, when to use Comment, Approve,
Request changes, how to leave a line comment, how to resolve a conflict.
**Done when**
- [ ] Written in your own words, with one real example from your PRs
- [ ] Linked from `## How we work` in the README

## Glossary of our topic  (Person C)
Branch: `docs/glossary`
**What:** `docs/glossary.md` with at least 8 terms: log, SIEM, event, alert, brute force, source IP,
threshold, false positive.
**Done when**
- [ ] Each term has 1-2 sentences, understandable for a classmate from another field
- [ ] Linked from the README
