# -*- coding: utf-8 -*-
"""Special matrix K.

2s on main diagonal, -1s on first sub-/super-diagonal.
Represents a system "fixed" at both ends.
"""

import logging
import numpy as np
import scipy.sparse
import scipy.linalg
from matrix import *


__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


__all__ = ["FixedFixed"]


_LOGGER = logging.getLogger(__name__)



class FixedFixed(IMatrix):
    """
    Fixed-fixed system matrix, defined by dimension.

    Such a matrix contains 2s along the main diagonal.
    It contains -1 along the both the superdiagonal and
    along the subdiagonal. Elsewhere, its entries are 0.

    """

    def __init__(self, n):
        """
        Create a *fixed-fixed* system special matrix `K`.

        Parameters
        ----------
        n : :obj:`int`
            Dimension for square matrix (row/column count).

        Raises
        ------
        :obj:`linalg.matrix.DimensionException`
            If the given size is less than 2.

        """
        if n < 2:
            raise DimensionException(
                    "Too small of dimension for {}: {}".
                    format(self.__class__.__name__, n))
        data = np.concatenate(
                (-1 * np.ones(n - 1),
                 2 * np.ones(n),
                 -1 * np.ones(n - 1)))
        index_pairs = \
                list(subdiagonal(n)) + \
                list(main_diagonal(n)) + \
                list(superdiagonal(n))
        self.matrix = scipy.sparse.csc_matrix(
                (data, zip(*index_pairs)), shape=(n, n))
        self._unit_solution = None


    def __getitem__(self, index):
        try:
            i, j = index
        except ValueError:
            raise MatrixIndexError(
                    "Specify pair of indices or use "
                    "colon-based syntax to select vector")
        if i == ":" and j == ":":
            return self.matrix
        return self.matrix[i, j]


    @property
    def n(self):
        """
        Get the side length of the underlying square matrix.

        Returns
        -------
        :obj:`int`
            Side length of the underlying square matrix.

        """
        return self.shape[0]


    @property
    def shape(self):
        """
        Determine the shape of the underlying matrix.

        Returns
        -------
        :obj:`tuple` of :obj:`int`
            Pair of row count and column count for matrix, should be equal.

        Raises
        ------
        :obj:`linalg.matrix.DimensionException`
            If the underlying matrix has been modified to not be square.

        """
        dims = self.matrix.shape
        if len(dims) != 2:
            raise DimensionException(
                    "Not two dimensions: {}".format(len(dims)))
        if dims[0] != dims[1]:
            raise DimensionException(
                    "Not square: {} x {}".format(dims[0], dims[1]))
        return dims

    
    def solve_unit(self):
        """
        Solve this fixed system for the all-1s response vector.

        Returns
        -------

        Raises
        ------
        :obj:`numpy.linalg.linalg.LinAlgError`
            If this the underlying coefficient matrix has been
            tampered with such that it's singular / non-invertible

        """
        if self._unit_solution is None:
            return scipy.linalg.solve(
                    self.matrix, np.ones(shape=(self.matrix.shape[1], 1)))
        else:
            return self._unit_solution

