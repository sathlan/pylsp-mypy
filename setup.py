#!/usr/bin/env python
from setuptools import setup
from mypy_ls import _version

if __name__ == "__main__":
    setup(version=_version.__version__, long_description_content_type="text/x-rst")
