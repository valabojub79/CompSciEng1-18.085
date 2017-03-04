# -*- coding: utf-8 -*-
"""Special matrix K.

2s on main diagonal, -1s on first sub-/super-diagonal.
Represents a system "fixed" at both ends.
"""

import numpy as np
import scipy.sparse
import scipy.linalg


__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"



def subdiagonal(n):
    """
    Generate the indices of the subdiagonal for n x b square matrix.

    Parameters
    ----------
    n : int
        Length of subdiagonal.

    Returns
    -------
    generator(int)
        Indices of the subdiagonal for n x b square matrix.

    """
    for i in range(1, n):
        yield i, i -1


def main_diagonal(n):
    """
    Generate the indices of the main diagonal for n x b square matrix.

    Parameters
    ----------
    n : int
        Length of main diagonal.

    Returns
    -------
    generator(int)
        Indices of the main diagonal for n x b square matrix.

    """
    for i in range(n):
        yield i, i



def superdiagonal(n):
    """
    Generate the indices of the superdiagonal for n x b square matrix.

    Parameters
    ----------
    n : int
        Length of superdiagonal.

    Returns
    -------
    generator(int)
        Indices of the superdiagonal for n x b square matrix.

    """
    for i in range(0, n - 1):
        yield i, i + 1



class FixedFixed(object):
    """
    Fixed-fixed system matrix, defined by dimension.

    Such a matrix contains 2s along the main diagonal.
    It contains -1 along the both the superdiagonal and
    along the subdiagonal. Elsewhere, its entries are 0.

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
        self.matrix = scipy.sparse.csc_matrix((data, index_pairs))
        self._unit_solution = None
        
    
    def solve_unit(self):
        """
        Solve this fixed system for the all-1s response vector.

        Returns
        -------

        Raises
        ------
        numpy.linalg.linalg.LinAlgError
            If this the underlying coefficient matrix has been
            tampered with such that it's singular / non-invertible

        """
        if self._unit_solution is None:
            return scipy.linalg.solve(self.matrix,
                                      np.ones(shape=(self.matrix.shape[1], 1)))
        else:
            return self._unit_solution

