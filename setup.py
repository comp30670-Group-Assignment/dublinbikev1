#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Group 2",
    author_email='timothy.madigan@ucdconnect.ie',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Software Engineering COMP30670 Project: Code files forGroup 2's submission for the Dublin Bikes project.",
    entry_points={
        'console_scripts': [
            'COMP30670ProjectDublinBikes=COMP30670ProjectDublinBikes.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='COMP30670ProjectDublinBikes',
    name='COMP30670ProjectDublinBikes',
    packages=find_packages(include=['COMP30670ProjectDublinBikes']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/comp30670-Group-Assignment/COMP30670ProjectDublinBikes',
    version='1.0',
    zip_safe=False,
)
