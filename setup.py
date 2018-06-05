#!/usr/bin/env python

from setuptools import setup, find_packages

DEPENDENCIES = [
    "bumpversion",
    "matplotlib",
    "numpy",
    "pytest",
    "scipy",
    "shapely",
]

setup(
    name='IPKISS',
    version='2.5',
    description='IPKISS Framework ce',
    author='Intec - Ugent',
    author_email='ipkiss@intec.ugent.be',
    url='www.ipkiss.org',
    license="GPL",
    extra_path="ipkiss"
    )
