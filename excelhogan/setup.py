# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.1.0'
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
     name='blockdiagcontrib-excelhogan',
     version=version,
     description='imagedrawer plugin for blockdiag',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['diagram','generator'],
     author='Takeshi Komiya',
     author_email='i.tkomiya at gmail.com',
     url='http://bitbucket.org/tk0miya/blockdiagcontrib',
     license='Apache License 2.0',
     packages=find_packages(),
     package_data = {'': ['buildout.cfg']},
     namespace_packages=['blockdiagcontrib'],
     include_package_data=True,
     install_requires=[
        'blockdiag>=1.2.0',
        'setuptools',
        'xlwt',
     ],
     entry_points="""
        [blockdiag_imagedrawers]
        excelhogan = blockdiagcontrib.excelhogan
     """,
)

