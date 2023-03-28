'''                       
Python package setup (used by Dockerfile).
'''

import os
import subprocess

from setuptools import setup, find_packages

data_files = []

setup(
    name='demo-cli',
    version='1.0',
    description='Sawtooth Demo Example',
    author='UBgood',
    url='https://github.com/UBgood/sawtooth-demo',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'colorlog',
        'protobuf',
        'sawtooth-sdk',
        'sawtooth-signing',
        'PyYAML',
    ],
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'demo = demo_cli:main_wrapper',
        ]
    })

