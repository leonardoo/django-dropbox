#!/usr/bin/env python
import os
from django_dropbox import get_version
from setuptools import setup, find_packages


requires = ['dropbox>=2.0.0', "urllib3>=1.10.1"]

setup(
    name='django-dropbox',
    version=get_version(),
    description='A Django App that contains a Django Storage which uses Dropbox.',
    author='Andres Torres Marroquin',
    author_email='andres.torres.marroquin@gmail.com',
    url='https://github.com/andres-torres-marroquin/django-dropbox',
    packages=find_packages(),
    install_requires=requires,
    license='BSD',
)
