"""Parse one log line into a dict. Owner: TC (feature/parser)."""
import ipaddress
import re
from datetime import datetime

EVENT_RE = re.compile(r"^[A-Z][A-Z_]*$")


def parse_line(line):
    """Turn '2026-11-09 10:15:02 192.0.2.10 FAILED_LOGIN admin' into a dict.

    Returns None for anything invalid (empty line, too few fields, bad IP,
    bad timestamp, bad event name). Log lines are untrusted input, so this
    function must never raise.
    """
    if not isinstance(line, str):
        return None
    parts = line.split()
    if len(parts) != 5:
        return None
    date_s, time_s, ip_s, event, user = parts
    try:
        datetime.strptime(f"{date_s} {time_s}", "%Y-%m-%d %H:%M:%S")
        ipaddress.ip_address(ip_s)
    except ValueError:
        return None
    if not EVENT_RE.match(event):
        return None
    return {"timestamp": f"{date_s} {time_s}", "ip": ip_s, "event": event, "user": user}
