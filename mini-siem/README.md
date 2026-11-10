# Mini SIEM

## What this is

A small Python web app for our team project. You paste fake log lines, the app stores them
and shows event counts, the top source IPs, and alerts for repeated failed logins.
It uses only made-up data (IPs from `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`).

## How to run it

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 and paste the content of `sample_logs.txt`.
Run the tests with `python -m pytest`.

More: [docs/how-to-run.md](docs/how-to-run.md)

## Team

<!-- Each person adds ONE row in their first PR. All three GitHub usernames must be here. -->

| Name | GitHub username | Parts |
|---|---|---|
| Ludwig | @Lurex225 | Log form, top IPs, README and CHANGELOG |
| TC | @tadiwachihota877-byte | Parser, storage, review guide |
| Ramon | @rafervi | Sample logs, event counts, alerts, glossary |

## How we work

- Every piece of work starts as an issue. Epics have the label `epic`.
- One issue, one branch (`feature/...` or `docs/...`), one pull request.
- The PR description says what and why and contains `closes #n`.
- Nobody pushes to `main`. Every PR needs 1 approval.
- Every PR adds one line to `CHANGELOG.md`.
- Commit messages say what changed ("Add parse_line for auth log format").
- Conflicts are solved on the laptop: merge `main` into the branch, fix, push.
- Reviews: see [docs/how-we-review.md](docs/how-we-review.md)

## Sources

| Date | Source | What we used it for |
|---|---|---|
| 2026-11-10 | Flask documentation | Routes, templates, forms |
| 2026-11-10 | Python docs: `sqlite3`, `ipaddress`, `collections.Counter` | Storage, IP validation, counting |

## Use of AI

| Date | Tool | What for | How we checked it |
|---|---|---|---|
| 2026-11-09 | Claude | Project idea, split of tasks, drafts of issue texts and README template | Team read it, changed it to fit our repo and rules |
| 2026-11-10 | Claude | Reference code for parser, storage, detection, app and tests; Git command guide | TODO: write what you really did (ran the tests, read every line, changed X) |
