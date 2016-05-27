"""
time.py
=======

Functions related to time and timing.
"""
import time


def time_since(then):
    """Compute the time since 'then'."""
    # Convert to epoch time
    if isinstance(then, time.struct_time):
        then = time.mktime(then)
    return time.mktime(time.localtime()) - then


def fmt_time_since(t):
    """Return a human-readable formatting of 'time since'."""
    if isinstance(t, time.struct_time):
        t = time.gmtime(t)

    s = "{:d} hours, {:d} minutes, {:d} seconds".format(
            t.tm_hours, t.tm_min, t.tm_sec)
    return s
