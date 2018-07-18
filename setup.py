""" install ipkiss packages and its dependencies """

from setuptools import setup, find_packages

DEPENDENCIES = [
    "bumpversion",
    "matplotlib",
    "numpy",
    "pytest",
    "pytest-html",
    "pyyaml",
    "scipy",
    "shapely",
    "sphinx",
    "sphinx_rtd_theme",
    "sphinxcontrib-napoleon",
    "tox"
]

setup(
    name="ipkiss",
    version="2.5.0",
    packages=find_packages(),
    install_requires=DEPENDENCIES,
)

