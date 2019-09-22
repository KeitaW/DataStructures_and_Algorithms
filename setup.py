from setuptools import setup
from setuptools import find_packages

# with open("README.md", "r") as f:
#    long_description = f.read()

setup(
    name="leetcode",
    version="develop",
    description="Log of leet codes.",
    author="Keita Watanabe",
    maintainer_email="keitaw09@gmail.com",
    # install_requires=[
    #    "dataclasses~=0.6",
    #    "ruamel.yaml~=0.15.99",
    #    "numpy~=1.16.4",
    #    "scipy~=1.2.1",
    #    "torch~=1.2.0",
    # ],
    packages=find_packages(),
)
