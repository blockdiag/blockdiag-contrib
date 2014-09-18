# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.1.0'
requires = ['blockdiag >= 1.4.3']
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
    name='blockdiagcontrib-octicons',
    version=version,
    description='octicons plugin for blockdiag',
    long_description=open("README.rst").read(),
    classifiers=classifiers,
    keywords=['diagram', 'generator'],
    author='Takeshi Komiya',
    author_email='i.tkomiya at gmail.com',
    url='http://bitbucket.org/blockdiag/blockdiag-contrib',
    license='Apache License 2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points="""
       [blockdiag_plugins]
       octicons = blockdiagcontrib.octicons
    """,
)
