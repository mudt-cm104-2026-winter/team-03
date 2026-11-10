from parser import parse_line


def test_valid_line():
    assert parse_line("2026-11-09 10:15:02 192.0.2.10 FAILED_LOGIN admin") == {
        "timestamp": "2026-11-09 10:15:02", "ip": "192.0.2.10",
        "event": "FAILED_LOGIN", "user": "admin"}


def test_empty_and_broken_lines_return_none():
    assert parse_line("") is None
    assert parse_line("   ") is None
    assert parse_line("only three fields here") is None
    assert parse_line("2026-11-09 10:15:02 999.1.1.1 LOGIN_OK bob") is None   # bad IP
    assert parse_line("2026-13-45 10:15:02 192.0.2.10 LOGIN_OK bob") is None  # bad date
    assert parse_line(None) is None
