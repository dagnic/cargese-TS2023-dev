"""
tools.py
"""
import datetime


def timestamp_to_datetime(timestamp: int) -> datetime.datetime:
    """
    Convert the timestamp in seconds since the Unix epoch
    which is January 1, 1970, 00:00:00 UTC to datetime object
    :param timestamp: input timestamp
    """
    return datetime.datetime.utcfromtimestamp(timestamp)
