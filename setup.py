# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.1.0'

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Python Software Foundation License",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
     name='blockdiagcontrib-square',
     version=version,
     description='renderer plugin for blockdiag',
     long_description='renderer plugin for blockdiag',
     classifiers=classifiers,
     keywords=['diagram','generator'],
     author='',
     author_email='',
     url='',
     license='PSL',
     packages=find_packages('blockdiagcontrib'),
     package_data = {'': ['buildout.cfg']},
     include_package_data=True,
     install_requires=[
        'blockdiag',
     ],
     entry_points="""
        [blockdiag_noderenderer]
        square = blockdiagcontrib.square
     """,
)

