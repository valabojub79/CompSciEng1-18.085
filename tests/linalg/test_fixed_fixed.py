"""
Tests for special matrix `K`, representing a "fixed-fixed" system.

Special matrix `K` is one of "second differences," representing a
system "fixed at both ends," as Prof. Strang says. This matrix has
2s on its main diagonal and -1s on the subdiagonal and superdiagonal.

"""

import pytest
from delacourse.linalg import FixedFixed

__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"



class FixedFixedConstructorTests:
    """
    Tests for the instantiation of special matrix `K`.
    """

    @pytest.mark.parametrize(argnames="n", argvalues=[])
    def test_dimension(self, n):
        """ Matrix dimension should match specification. """
        assert n == FixedFixed(n).n
        assert (n, n) == FixedFixed(n).shape


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

    def test_accuracy(self):
        """ The solver should be accurate. """
        pass


    def test_solution_attribute(self):
        """ The solver should establish a solutions attribute. """
        pass


    def test_min_work(self):
        """ If the solution's been set, do no further work. """
        pass
