#!/usr/bin/env python3
import subprocess
from setuptools import find_packages, setup


def version():
    """Read version from Git tag, falling back to .version file."""
    try:  # Use latest git tag
        version = subprocess.check_output(
            ['git', 'describe', '--tags']).decode().rstrip()
        with open('./.version', 'w') as f:
            print("Storing {} in .version".format(version))
            f.write(version)
        return version
    except subprocess.CalledProcessError:  # No git repo; likely installing
        try:
            with open('./.version', 'r') as f:  # Read from .version file
                return f.read().rstrip()
        except FileNotFoundError:  # Didn't get packaged with a .version file
            print("No .git directory or .version file found; defaulting")
            return '0.0.1'

setup(
    name='Toolbox',
    author='jad-b',
    url='https://github.com/jad-b/toolbox',
    packages=find_packages(),
    include_package_data=True,
    license='LGPL',
    version=version(),
    description='The tools I always wished I had on hand',
    entry_points={
        'console_scripts': ['toolbox=toolbox.main:main']
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
