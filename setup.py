#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


from distutils.core import setup

import omnijson


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()


if sys.argv[-1] == 'speedups':
    try:
        __import__('pip')
    except ImportError:
        print('Pip required.')
        sys.exit(1)

    os.system('pip install ujson')
    sys.exit()

setup(
    name='omnijson',
    version=omnijson.__version__,
    description='''Wraps the best JSON installed, falling back on an
    internal simplejson.''',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/omnijson',
    packages=[
        'omnijson',
        'omnijson.packages',
        'omnijson.packages.simplejson'
    ],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
    ),
)
