#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='0.0.1',
    description='Nameko Hello World',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        "nameko>=2.1.2",
        "python-memcached>=1.54"
    ],
    extras_require={
        'dev': [
            "pytest==2.4.2",
            "mockcache==1.0.1"
        ],
    },
    zip_safe=True
)
