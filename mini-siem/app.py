"""Mini SIEM web app (Flask).

Blocks are marked with the PR that adds them, so each person can add their own
part in their own branch. Delete the [markers] before you commit.
"""
from flask import Flask, render_template, request

from parser import parse_line                                   # [storage] TC
from db import init_db, save_entries, get_entries               # [storage] TC
from detect import count_by_event, top_ips, find_alerts         # [count/top-ips/alerts]

app = Flask(__name__)
init_db()                                                       # [storage] TC


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":                                # [log-form] Ludwig
        text = request.form.get("logs", "")
        lines = [ln for ln in text.splitlines() if ln.strip()]
        message = f"Received {len(lines)} lines."
        entries = [e for e in (parse_line(ln) for ln in lines) if e]   # [storage] TC
        save_entries(entries)                                          # [storage] TC
        message = f"Received {len(lines)} lines, saved {len(entries)} valid entries."  # [storage] TC

    entries = get_entries()                                     # [storage] TC
    return render_template(
        "index.html",
        message=message,
        total=len(entries),
        counts=count_by_event(entries),                         # [count-events] Ramon
        top=top_ips(entries),                                   # [top-ips] Ludwig
        alerts=find_alerts(entries),                            # [alerts] Ramon
    )


if __name__ == "__main__":
    app.run(debug=True)   # http://127.0.0.1:5000, local use only
