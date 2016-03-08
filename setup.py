#!/usr/bin/env python3
import subprocess
from setuptools import find_packages, setup


setup(
    name='Toolbox',
    author='jad-b',
    url='https://github.com/jad-b/toolbox',
    include_package_data=True,
    license='LGPL',
    version=subprocess.check_output(['git', 'describe', '--tags']),
    description='The tools I always wished I had on hand',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
