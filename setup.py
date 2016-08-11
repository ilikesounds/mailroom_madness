# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='Mail_Room_Madness',
    description='A Python script for the SEA PY401d4 course.',
    version=0.1,
    author='Jeff Torres, Adam Palmer',
    author_email='email@email.com',
    license='MIT',
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
