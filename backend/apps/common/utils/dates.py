from datetime import date


def days_between(d1: date, d2: date) -> int:
    return abs((d2 - d1).days)
