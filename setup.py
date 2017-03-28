#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
import os.path


def read_requirements(pathname):
    with open(pathname) as f:
        return [line for line in (x.strip() for x in f) if not line.startswith('#')]


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)

setup(
    name='RealOne',
    version='1.0.0',
    description="Boilerplate for RealOne",
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.md',
    )),
    author="sean.clooney",
    author_email='sean.clooney@bloombergpolarlake.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=read_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt')),
    license='(c) Bloomberg PolarLake, all rights reserved',
    data_files=[('', glob.glob(project_path('*.txt')), glob.glob(project_path('*.rst')))],
    zip_safe=False,
    keywords='realone',
    classifiers=[
        'Private :: Do Not Upload',
        'License :: (c) Bloomberg PolarLake, all rights reserved',
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='nose.collector',
    entry_points={
        'console_scripts': ['something_meaningful=realone:print_1_to_10']
    }
)
