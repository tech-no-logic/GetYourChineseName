# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='get-your-chinese-name',
    version='0.0.1',
    description='Application to generate a Chinese Name',
    long_description=readme,
    author='tech-no-logic',
    author_email='tnl.hanlin@gmail.com',
    url='https://github.com/tech-no-logic/GetYourChineseName',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)