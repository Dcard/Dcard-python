from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="dcard",
    version="0.1.0",
    description="Dcard python module",
    license="MIT",
    author="Dcard",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description
)
