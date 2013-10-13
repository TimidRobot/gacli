#!/usr/bin/env python
try:
    # Third-party
    from setuptools import setup
except ImportError:
    # Standard library
    from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name="gacli",
      version="1.0.1",
      description="Google Authentication command line tools",
      long_description=long_description,
      author="Timid Robot Zehta",
      author_email="tim@clockwork.net",
      url="https://github.com/ClockworkNet/gacli/",
      scripts=["ga"],
      classifiers=["Environment :: Console",
                   "Intended Audience :: System Administrators",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Topic :: Security",
                   "Topic :: Utilities",
                   ],
      install_requires=["onetimepass"],
      )
