# vim: set fileencoding=utf-8 :

"""gacli setup
"""

# Standard library
from __future__ import absolute_import, division, print_function
try:
    # Third-party
    from setuptools import setup
except ImportError:
    # Standard library
    from distutils.core import setup

with open("README.rst", "rb") as file:
    long_description = file.read().decode("utf-8")

classifiers = ["Environment :: Console",
               "Intended Audience :: System Administrators",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: MIT License",
               "Natural Language :: English",
               "Operating System :: MacOS :: MacOS X",
               "Operating System :: POSIX :: Linux",
               "Programming Language :: Python :: 2",
               "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 3",
               "Programming Language :: Python :: 3.5",
               "Programming Language :: Python :: Implementation :: CPython",
               "Topic :: Security",
               "Topic :: Utilities"]

setup(author="Timid Robot Zehta",
      author_email="tim@clockwork.net",
      classifiers=classifiers,
      description="Google Authentication command line tools",
      install_requires=["onetimepass"],
      long_description=long_description,
      name="gacli",
      scripts=["ga"],
      url="https://github.com/ClockworkNet/gacli/",
      version="1.0.3",
      )
