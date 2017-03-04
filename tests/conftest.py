"""Project-wide test configuration.
"""

__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


NAME_RANDOM_SIZE = "randsize"



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
    parser.addoption("--{}".format(NAME_RANDOM_SIZE), type=int, default=10,
                     help="For tests requesting parameterization with respect "
                          "to randomized input data sizes, the number of "
                          "random values to generate and thus the number "
                          "of parameterized test case instances to execute")



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
    if NAME_RANDOM_SIZE in metafunc.fixturenames():
        # Default handled in option definition
        num_random = getattr(metafunc.config.option, NAME_RANDOM_SIZE)
        metafunc.parametrize(NAME_RANDOM_SIZE, num_random)
