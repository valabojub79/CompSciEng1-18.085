# -*- coding: utf-8 -*-
"""
Project-wide test configuration.
"""

import logging
import os
import numpy.random as nprand
import pytest
from delacourse import setup_project_logger

__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


NAME_RANDOM_SIZE = "num-random"
LOGLEVEL_OPTNAME = "--logging-level"
MAX_RANDOM_DIMENSION = 10001

_LOGGER = logging.getLogger(__name__)



@pytest.fixture(scope="session")
def session_logging(request):
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
    parser : pytest._pytest.config.Parser
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
    if random_dimension.__name__ in metafunc.fixturenames:
        # Default handled in option definition
        num_random = getattr(metafunc.config.option,
                             NAME_RANDOM_SIZE.replace("-", "_"))
        try:
            metafunc.parametrize(
                    random_dimension.__name__,
                    nprand.randint(low=2, high=MAX_RANDOM_DIMENSION,
                                   size=num_random))
        except AttributeError:
            # DEBUG
            _LOGGER.error("METAFUNC: {}".format(dir(metafunc)))
            _LOGGER.error("PARAMETRIZE: {}".format(dir(metafunc.parametrize)))
            print("METAFUNC: {}".format(dir(metafunc)))
            print("PARAMETRIZE: {}".format(dir(metafunc.parametrize)))
            raise



@pytest.fixture(scope="function")
def random_dimension():
    return nprand.randint(MAX_RANDOM_DIMENSION)
