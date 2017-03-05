# -*- coding: utf-8 -*-
"""
Working with matrices.
"""

__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


__all__ = ["main_diagonal", "subdiagonal", "superdiagonal"]



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
        yield i, i - 1


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
