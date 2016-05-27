"""
timer.py
========
A code block timer implemented as a context manager.
"""
import time


class Timer(object):

    def __init__(self, func):
        self.func = func
        self.start_time = None
        self.end_time = None
        self.length = None

    def __call__(self, *args, **kwargs):
        with self:
            result = self.func(*args, **kwargs)
        return result

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.length = self.end_time - self.start_time

    def __str__(self):
        if self.length is None:     # Still running
            curr_len = time.time() - self.start_time
            return 'Code has been running for {} seconds'.format(curr_len)
        else:
            return 'Code ran in {} seconds'.format(self.length)
