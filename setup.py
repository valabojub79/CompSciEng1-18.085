# -*- coding: utf-8 -*-
"""
Setup script for delacourse package.

The package contains code relating to
"""

import os
from setuptools import find_packages, setup


PROJECT_NAME = "delacourse"


class _VersionNotFoundException(Exception):
    def __init__(self, path_searched_file):
        super("Found no version information in '{}'".
              format(path_searched_file))


def discover_version():
    """
    Discover the project version by parsing a version file.

    Returns
    -------
    str
        The version information discovered from the searched file.

    """
    path_version_file = os.path.join("delacourse", "_version.py")
    with open(path_version_file, 'r') as versionfile:
        for line in versionfile:
            if line.startswith("__version__"):
                v = line.split(" = ")[1].strip("\n \"'")
                break
        else:
            raise _VersionNotFoundException(path_version_file)
    return v


version = discover_version()


setup(name=PROJECT_NAME,
      description="Differential equations and linear algebra",
      long_description="Differential equations and linear algebra, "
                       "inspired by lectures, readings, and exercises from "
                       "MIT OCW 18.085 (Computational Science and "
                       "Engineering I), as taught in Fall 2008 by "
                       "Professor Gilbert Strang.",
      url="https://github.com/vreuter/CompSciEng1-18.085",
      author="Vince Reuter",
      author_email="vince.reuter@gmail.com",
      license="MIT",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: The Curious",
          "Topic :: Math :: Scientific Computing",
          "License :: OSI Approved :: MIT"
      ],
      keywords="math diffeq 'differential equations' 'linear algebra'",
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      install_requires=["numpy", "scipy"])
