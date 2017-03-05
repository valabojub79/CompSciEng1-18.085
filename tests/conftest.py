# -*- coding: utf-8 -*-
"""
Project-wide test configuration.
"""

import logging
import os
import pytest
from delacourse import setup_project_logger


__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


_LOGGER = logging.getLogger(__name__)
NAME_RANDOM_SIZE = "num-random"
LOGLEVEL_OPTNAME = "--logging-level"



@pytest.fixture(scope="session")
def session_logging(request):
    """ Establish logger for the testing session. """
    setup_project_logger(level=request.config.getoption(LOGLEVEL_OPTNAME))
    global _LOGGER
    _LOGGER = logging.getLogger(
            "{}.{}".format("delacourse",
                           os.path.split(os.path.dirname(__file__))[1]))



def pytest_addoption(parser):
    """
    Augment the option/argument space of the pytest argument parser.

    This if a communication interface for adding nice features like
    specifying test speed tolerance, number of randomized cases to
    generate for tests requesting random data, logging level etc.

    Parameters
    ----------
    parser : :obj:`pytest._pytest.config.Parser`
        The command-line argument parser used by pytest.

    """
    parser.addoption("--{}".format(NAME_RANDOM_SIZE),
                     type=int, default=10,
                     help="For tests requesting parameterization with respect "
                          "to randomized input data sizes, the number of "
                          "random values to generate and thus the number "
                          "of parameterized test case instances to execute")
    parser.addoption(LOGLEVEL_OPTNAME, default=logging.DEBUG,
                     help="Logging level for testing session")



def pytest_generate_tests(metafunc):
    """
    Enable dynamic test case parameterization based on
    requested fixtures and command-line arguments.

    Parameters
    ----------
    metafunc : pytest._pytest.python.Metafunc
        Test case function metadata encapsulation permitting
        access to some information about a case and allowing
        dynamic modification of it.

    """
    if "random" in metafunc.fixturenames:
        # Default setting is handled in option definition.
        num_random = getattr(metafunc.config.option,
                             NAME_RANDOM_SIZE.replace("-", "_"))
        generator = getattr(metafunc.function, "random").args[0]
        metafunc.parametrize("random", generator.build(num_random))



class RandomParams(object):
    """
    Provide random value parameterization for a test case.

    This small class provides an interface through which a test case
    can specify a request for randomized parameterization. This is
    accomplished by leveraging pytest's marking mechanism and using
    the :obj:`Metafunc` object available in the :obj:`pytest_generate_tests`
    hook. The random data generation function and arguments are
    designated by tagging a test case with  :obj:`pytest.mark.random`
    and building an instance of this class. The instance of this class
    is then available within the :obj:`MarkInfo` object that's accessible
    in :obj:`pytest_generate_tests`. To get at the generation data stored
    here, the tests generation function calls
    :obj:`getattr(metafunc.function)`, passing "random" as the second
    argument (this is the name for this special mark and the fixture
    name that the tests generator looks for to determine whether it
    needs to build the random parameter arguments.

    """


    def __init__(self, func, args=None, kwargs=None, max_tests=float("inf")):
        """
        Define the parameterization mechanism with a function and arguments.

        Parameters
        ----------
        func : :obj:`callable`
            The function responsible for generating the random arguments.
        args : :obj:`tuple`
            Positional arguments to pass to :obj:`func`.
        kwargs : :obj:`dict`
            Keyword arguments to pass to :obj:`func`.
        max_tests : :obj:`int`
        """
        super(RandomParams, self).__init__()
        self.f = func
        self.args = args or tuple()
        self.kwargs = kwargs or dict()
        self.limit = max_tests


    def build(self, n):
        """
        Create n random argument values for a parameter.

        Parameters
        ----------
        n : :obj:`int`
            Number of random argument values to generate for a parameter.

        Returns
        -------
        :obj:`list`
            List of random arguments for a parameter, of requested size.

        """
        num_values = min(n, self.limit)
        _LOGGER.debug("Creating %d arguments (limit=%d, requested=%s)",
                      num_values, self.limit, n)
        return [self.f(*self.args, **self.kwargs) for _ in range(num_values)]
