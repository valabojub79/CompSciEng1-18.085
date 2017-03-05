"""
Random mishmash of utilities.
"""

import sys

__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


def minint():
    """
    Get the minimum integer value.

    Returns
    -------
    int
        Minimum integer value.

    """
    return -maxint()


def maxint():
    """
    Get the maximum integer value.

    Returns
    -------
    int
        Maximum integer value.

    """
    return sys.maxint if sys.version_info < 3 else sys.maxsize
