"""
This file configures the Python package with entrypoints used for future runs on Databricks.

Please follow the `entry_points` documentation for more details on how to configure the entrypoint:
* https://setuptools.pypa.io/en/latest/userguide/entry_point.html
"""

from setuptools import find_packages, setup

# parse_requirements() returns generator of pip.req.InstallRequirement objects
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="src",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=required,
    setup_requires=["wheel"],
    version="0.0.1",
    description="",
    author="",
)
