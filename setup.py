#!/usr/bin/env python

import os
import sys
from distutils.core import setup

__author__ = 'Bhanu Vattikonda <bvattikonda@cs.ucsd.edu>'
__version__ = '1.0.0'

packages = ['pyreads']

setup(name = 'PyReads',
      version = __version__,
      install_requires = ['oauth2>=1.5.211'],
      description = 'Python interface to the GoodReads API',
      author = 'Bhanu Vattikonda',
      author_email = 'bvattikonda@cs.ucsd.edu',
      url = 'http://cseweb.ucsd.edu/~bvattikonda/',
      packages = packages,
     )
