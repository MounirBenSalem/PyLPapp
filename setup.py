# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PyLPapp',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Mounir Bensalem',
    author_email='mounirsalem123@yahoo.fr',
    url='https://github.com/MounirBenSalem/PyLPapp',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)