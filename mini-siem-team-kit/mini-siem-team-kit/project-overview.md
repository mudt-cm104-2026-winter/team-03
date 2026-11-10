# What the finished project looks like

## 1. The app

```
┌─────────────────────────────────────────────────────┐
│  Mini SIEM                                          │
│                                                     │
│  Paste log lines (one per line):                    │
│  ┌───────────────────────────────────────────────┐  │
│  │2026-11-09 10:15:02 192.0.2.10 FAILED_LOGIN root│ │
│  │2026-11-09 10:15:09 192.0.2.10 FAILED_LOGIN admin││
│  └───────────────────────────────────────────────┘  │
│  [ Analyze ]                                        │
│                                                     │
│  ⚠ HIGH: 192.0.2.10 had 4 failed logins             │
│                                                     │
│  Events (30 total)        Top source IPs            │
│  FAILED_LOGIN   6         192.0.2.10      6         │
│  LOGIN_OK       18        198.51.100.7    9         │
│  LOGOUT         6         203.0.113.4     5         │
└─────────────────────────────────────────────────────┘
```

Flow: paste -> parse (B) -> save in SQLite (B) -> count, rank and alert (A, C) -> show on the page (A).

## 2. The repository on `main` (names may differ with the existing app)

```
team-NN/
├── app.py                  # web app, routes (A)
├── templates/index.html    # the page above (A)
├── parser.py               # parse_line (B)
├── db.py                   # SQLite save/load (B)
├── detect.py               # count, top IPs, alerts (C, A)
├── sample_logs.txt         # fake data with one attack (C)
├── docs/
│   ├── how-to-run.md       # (A)
│   ├── how-we-review.md    # (B)
│   └── glossary.md         # (C)
├── CHANGELOG.md            # one line per PR
├── README.md               # 6 required sections
└── .gitignore
```

## 3. GitHub at the deadline

- Board in the repo (Projects tab): 3 epics and 10 sub-issues, all in Done
- About 10 merged PRs, each linked to a closed issue with `closes #n`
- 1 PR with a Request changes review and the fix after it
- 1 PR showing the merge commit that solved the conflict
- Reviews with line comments from all three people
- Tag `stage-1` listed under Tags

## The idea in one picture

```
Issue -> Branch -> Commits -> Pull request -> Review -> Merge into main
(A,B,C)  (own)     (small)    (closes #n)    (teammate)   (protected)
                                                               |
                                                     Tag stage-1 (C)
```
