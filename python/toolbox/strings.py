import random
import string


def randstring(n):
    """Generate an _n_-length random string.

    Arguments:
        n (int): Length of string to return.

    Returns:
        str: A string of length _n_.

    Source: http://stackoverflow.com/a/2257449
    """
    return ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits) for _ in range(n))
