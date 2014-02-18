#!/usr/bin/env python
try:
    # Third-party
    from setuptools import setup
except ImportError:
    # Standard library
    from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(author="Timid Robot Zehta",
      author_email="tim@clockwork.net",
      classifiers=["Environment :: Console",
                   "Intended Audience :: System Administrators",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Topic :: Security",
                   "Topic :: Utilities",
                   ],
      description="Google Authentication command line tools",
      install_requires=["onetimepass"],
      long_description=long_description,
      name="gacli",
      scripts=["ga"],
      url="https://github.com/ClockworkNet/gacli/",
      version="1.0.2",
      )
