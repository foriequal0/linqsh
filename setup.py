#!/usr/bin/env python

from distutils.core import setup
import sys

print(sys.argv)
setup(
    name='linqsh',
    version='1.0',
    description='LINQ for shell',
    author='SeongChan Lee',
    author_email='foriequal@gmail.com',
    install_requires=['asq'],
    classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'Environment :: Console',
      'Programming Language :: Python :: 3 :: Only'
    ],
    entry_points={
      'console_scripts': [
          'linqsh=linqsh.main:main',
          # TODO : flag --symlink or something
          'filter=linqsh.main:main',
          'from_stdin=linqsh.main:main'
          'foreach=linqsh.main:main'
          ]},
    )
