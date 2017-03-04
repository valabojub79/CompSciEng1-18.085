"""Special matrix K.

2s on main diagonal, -1s on first sub-/super-diagonal.
Represents a system "fixed" at both ends.

"""

import numpy as np
from scipy.sparse import csc_matrix

__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"



def subdiagonal(n):
    for i in range(1, n):
        yield i, i -1


def main_diagonal(n):
    for i in range(n):
        yield i, i



def superdiagonal(n):
    for i in range(0, n - 1):
        yield i, i + 1



class FixedFixed(object):
    """Fixed-fixed system matrix, defined by dimension.

    """

    def __init__(self, n):
        """Create a *fixed-fixed* system special matrix `K`.

        Parameters
        ----------
        n : int
            Dimension for square matrix (row/column count).

        """
        data = np.concatenate(
                (-1 * np.ones(n - 1), 2 * np.ones(n), -1 * np.ones(n - 1)))
        index_pairs = \
                list(subdiagonal(n)) + \
                list(main_diagonal(n)) + \
                list(superdiagonal(n))
        self.matrix = csc_matrix((data, index_pairs))

