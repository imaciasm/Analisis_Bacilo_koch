from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
ext_modules = []
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
     long_description = f.read()

setup(
    name="Analisis_Bacilo_koch",
    version='1.0.0',
    description='Analisis Bacilo Koch ORFs',
    long_description=long_description,
    url="https://github.com/imaciasm/Analisis_Bacilo_koch",
    author='Ignacio Macias Martinez',
    author_email='imaciasm@uoc.edu',
    include_package_data=True,
    install_requires=["matplotlib", "coverage"]
)