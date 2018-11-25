from setuptools import setup, find_packages
import re
import subprocess

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='jinja2_auto_gen_code',
    version='1.0.0',
    description='Automatic generate the code',
    author='edmond',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
)
