from detect import count_by_event, top_ips, find_alerts


def e(ip, event):
    return {"timestamp": "2026-11-09 10:00:00", "ip": ip, "event": event, "user": "x"}


def test_empty_lists():
    assert count_by_event([]) == {}
    assert top_ips([]) == []
    assert find_alerts([]) == []


def test_count_by_event():
    assert count_by_event([e("192.0.2.1", "A"), e("192.0.2.1", "A"), e("192.0.2.2", "B")]) == {"A": 2, "B": 1}


def test_top_ips_sorted_and_limited():
    data = [e("192.0.2.1", "A")] * 3 + [e("192.0.2.2", "A")] * 2 + [e("192.0.2.3", "A")]
    assert top_ips(data, n=2) == [("192.0.2.1", 3), ("192.0.2.2", 2)]


def test_alerts_threshold():
    data = [e("192.0.2.10", "FAILED_LOGIN")] * 4 + [e("192.0.2.20", "FAILED_LOGIN")] * 2
    assert find_alerts(data) == ["HIGH: 192.0.2.10 had 4 failed logins"]
    assert len(find_alerts(data, threshold=2)) == 2
