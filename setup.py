#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = [
    'configargparse',
    'numpy',
    'scipy',
    'astropy>=4.1',
    'matplotlib',
    'pandas',
    'astroquery>0.4.1',
    'sep',
    'photutils',
    'statsmodels',
    'esutil',
    'tqdm',
    'regions'
]

setup(
    name='stdpipe',
    version='0.1',
    description='Simple Transient Detection Pipeline',
    author='Sergey Karpov',
    author_email='karpov.sv@gmail.com',
    url='',
    install_requires=requirements,
    packages=['stdpipe'],
    package_data={'stdpipe':['data/*']},
    include_package_data=True,
    extras_require={
        "example": [
            'astroscrappy',
            'regions',
            'tqdm',
        ],
    },    
)
