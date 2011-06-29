# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.1.1'
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
     name='blockdiagcontrib-qb',
     version=version,
     description='noderenderer plugin for blockdiag',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['diagram','generator'],
     author='Takeshi Komiya',
     author_email='i.tkomiya at gmail.com',
     url='http://tk0miya.bitbucket.org/blockdiag/build/html/index.html',
     license='PSL',
     packages=find_packages(),
     package_data = {'': ['buildout.cfg']},
     namespace_packages=['blockdiagcontrib'],
     include_package_data=True,
     install_requires=[
        'blockdiag>=0.8.2',
        'setuptools',
     ],
     entry_points="""
        [blockdiag_noderenderer]
        qb = blockdiagcontrib.qb
     """,
)

