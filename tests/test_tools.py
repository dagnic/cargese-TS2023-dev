"""
test_tools.py
"""
import datetime

from src.cargese import tools


def test_timestamp_to_datetime():
    utc_date = tools.timestamp_to_datetime(0)
    assert utc_date == datetime.datetime(1970, 1, 1)
