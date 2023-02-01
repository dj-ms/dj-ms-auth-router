#!/usr/bin/env python3.10
from setuptools import setup, find_packages

with open('README.md') as r:
    readme = r.read()

setup(
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
)
