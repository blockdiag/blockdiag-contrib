# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.1.3'
long_description = open("README.txt").read()

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
     description='noderenderer plugin for blockdiag',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['diagram','generator'],
     author='Takeshi Komiya',
     author_email='i.tkomiya at gmail.com',
     url='http://blockdiag.com/',
     license='PSL',
     packages=find_packages(),
     package_data = {'': ['buildout.cfg']},
     namespace_packages=['blockdiagcontrib'],
     include_package_data=True,
     install_requires=[
        'blockdiag>=1.1.0',
        'setuptools',
     ],
)

