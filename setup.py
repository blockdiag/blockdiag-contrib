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
     description='noderenderer plugin for blockdiag',
     long_description='noderenderer plugin for blockdiag',
     classifiers=classifiers,
     keywords=['diagram','generator'],
     author='Takeshi Komiya',
     author_email='i.tkomiya at gmail.com',
     url='http://tk0miya.bitbucket.org/blockdiag/build/html/index.html',
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

