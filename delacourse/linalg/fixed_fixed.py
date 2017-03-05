# -*- coding: utf-8 -*-
"""Special matrix K.

2s on main diagonal, -1s on first sub-/super-diagonal.
Represents a system "fixed" at both ends.
"""

import numpy as np
import scipy.sparse
import scipy.linalg
from matrix import main_diagonal, subdiagonal, superdiagonal


__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


__all__ = ["FixedFixed"]



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
        self.matrix = scipy.sparse.csc_matrix((data, zip(*index_pairs)))
        self._unit_solution = None


    @property
    def n(self):
        return self.shape[0]


    @property
    def shape(self):
        return self.matrix.shape

    
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

