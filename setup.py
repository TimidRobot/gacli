#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="gacli",
      version="1.0",
      description="Google Authentication command line tools",
      long_description=open("README.rst").read(),
      author="Tim Zehta",
      author_email="tim@clockwork.net",
      url="https://github.com/ClockworkNet/gacli/archive/master.zip#egg=gacli",
      scripts=["ga"],
      classifieres=["License :: OSI Approved :: MIT License"],
      install_requires=["onetimepass"],
      dependency_links=["https://github.com/tadeck/onetimepass/archive/v0.1.2.tar.gz#egg=onetimepass-0.1.2"]
      )
