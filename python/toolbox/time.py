"""
time.py
=======

Functions related to time and timing.
"""
import argparse
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


def s3time(args):
    """Un-optimize a timestamp from S3 format.

    Apparently, it is "better" to lop off the last 4 digits and reverse your
    timestamp when naming files in S3.
    """
    ts = args.timestamp
    fwd = ts[::-1]  # Un-reverse the timestamp
    full = fwd + ('0' * (10 - len(fwd)))  # Add truncated 0's
    x = time.gmtime(int(full))  # Convert to time.struct_time
    print("{} = {}".format(ts, time.strftime("%Y %b %d %H:%M", x)))


def parse(args):
    parser = argparse.ArgumentParser()
    subp = parser.add_subparsers()
    s3p = subp.add_parser("s3stamp")
    s3p.add_argument("timestamp", help="Reversed, truncate timestamp")
    s3p.set_defaults(func=s3time)

    args = parser.parse_args(args)
    args.func(args)
