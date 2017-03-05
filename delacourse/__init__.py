# -*- coding: utf-8 -*-
"""Differential equations + linear algebra CourSE).

MIT OCW 18.085, as taught in Fall 2008 by Professor Gilbert Strang.
"""

import logging
import os
import sys
from linalg import *


__author__ = "Vince Reuter"
__email__ = "vince.reuter@gmail.com"


LOG_FMT = "%(modname)s:%(lineno)d [%(levelname)%s] > %(message)s"


def setup_project_logger(level, locations=None):
    """
    Establish the project logging infrastructure.

    Parameters
    ----------
    level : str | int
        Name of logging level or integral value for it.
    locations : str | collections.Iterable[str]
        Where to write logs.

    Returns
    -------
    logging.Logger
        Configured project logger.

    """

    logger = logging.getLogger("delacourse")
    logger.setLevel(level)
    logger.propagate = False

    if locations:
        if isinstance(locations, str):
            locations = (locations, )
        else:
            locations = tuple(locations)
    else:
        locations = (sys.stderr, )

    for loc in locations:
        if isinstance(loc, str):
            dirpath = os.path.dirname(loc)
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
            handler = logging.FileHandler(loc, mode='w')
        else:
            handler = logging.StreamHandler(loc)
        handler.setLevel(level)
        logger.addHandler(handler)

    return logger
