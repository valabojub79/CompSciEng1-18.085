# -*- coding: utf-8 -*-
"""
Tests for special matrix `K`, representing a "fixed-fixed" system.

Special matrix `K` is one of "second differences," representing a
system "fixed at both ends," as Prof. Strang says. This matrix has
2s on its main diagonal and -1s on the subdiagonal and superdiagonal.

"""

import logging
import numpy.random as nprand
import pytest
from tests.conftest import RandomParams
from delacourse.linalg.fixed_fixed import FixedFixed
from delacourse.linalg.matrix import DimensionException
from delacourse import utils as delautils


__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


_LOGGER = logging.getLogger("{}.{}".format("delacourse", __name__))



class FixedFixedConstructorTests:
    """
    Tests for the instantiation of special matrix `K`.
    """

    @pytest.mark.parametrize(argnames="dim", argvalues=[0, 1])
    def test_small_nonnegative_dimension(self, dim):
        """ Empty Matrix K is prohibited. """
        with pytest.raises(DimensionException):
            FixedFixed(dim)


    @pytest.mark.random(
            RandomParams(nprand.randint,
                         kwargs={"low": delautils.minint(), "high": 0}))
    def test_negative_dimension(self, random):
        """ Singleton K is prohibited. """
        with pytest.raises(DimensionException):
            FixedFixed(random)


    @pytest.mark.random(
            RandomParams(nprand.randint, max_tests=5,
                         kwargs={"low": 2, "high": 10001}))
    def test_valid_dimension(self, random):
        """ Matrix dimension should match specification. """
        assert random == FixedFixed(random).n
        assert (random, random) == FixedFixed(random).shape


    def test_ones_null_solution(self):
        """ Initially, solution to all-1s vector is null. """
        pass


    def test_invertibility(self):
        """ This special matrix is invertible. """
        pass



class FixedFixedSolveOnesTests:
    """
    Tests for solving system in which `K` is the coefficient matrix.
    """


    def test_empty(self):
        pass


    def test_single(self):
        pass


    def test_accuracy(self):
        """ The solver should be accurate. """
        pass


    def test_solution_attribute(self):
        """ The solver should establish a solutions attribute. """
        pass


    def test_min_work(self):
        """ If the solution's been set, do no further work. """
        pass
