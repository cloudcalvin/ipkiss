""" install ipkiss packages and its dependencies """

from setuptools import setup, find_packages

DEPENDENCIES = [
    "Pillow",
    "bumpversion",
    "click",
    "jinja2",
    "matplotlib",
    "numpy",
    "psycopg2",
    "psycopg2-binary",
    "pyqtree",
    "pyqtree",
    "pytest",
    "pytest-html",
    "pyyaml",
    "recommonmark",
    "scipy",
    "shapely",
    "sphinx",
    "sphinx_rtd_theme",
    "sphinxcontrib-napoleon",
    "tqdm",
    "tox"
]

setup(
    name="ipkiss",
    version="2.5.0",
    packages=find_packages(),
    install_requires=DEPENDENCIES,
)

