"""Analysis functions. Owners: Ramon (count_by_event, find_alerts), Ludwig (top_ips)."""
from collections import Counter


# --- Ramon: feature/count-events ---
def count_by_event(entries):
    """{'FAILED_LOGIN': 5, 'LOGIN_OK': 2}. Empty list gives {}."""
    return dict(Counter(e["event"] for e in entries))


# --- Ludwig: feature/top-ips ---
def top_ips(entries, n=5):
    """[(ip, count), ...] with the most active IP first, at most n rows."""
    return Counter(e["ip"] for e in entries).most_common(n)


# --- Ramon: feature/alerts ---
def find_alerts(entries, threshold=3):
    """One message per IP with at least `threshold` FAILED_LOGIN events."""
    failed = Counter(e["ip"] for e in entries if e["event"] == "FAILED_LOGIN")
    return [
        f"HIGH: {ip} had {count} failed logins"
        for ip, count in failed.most_common()
        if count >= threshold
    ]
