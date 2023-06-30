"""Setup file for the ADAD package

To install this local package
    python -m pip install -e .

TODO: Add the list of required packages
"""
from setuptools import setup, find_packages

setup(
    name='adad',
    description='Applicability Domain & Adversarial Defences',
    packages=find_packages(),
    version='0.0.1',
    python_requires='>=3.8',
)
