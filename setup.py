#!/usr/bin/env python3

import os
from os import chdir
from os.path import join, dirname, normpath, abspath
from setuptools import find_packages, setup

with open(join(dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name='django-open-iconic',
    version='1.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT/SIL License',
    description='Open Iconic web font packaged for Django',
    long_description=README,
    author='Ryan Marquardt',
    author_email='ryan.marquardt@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
