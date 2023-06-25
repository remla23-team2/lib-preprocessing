from setuptools import find_packages, setup

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

setup(
    name='lib_preprocessing_REMLA23_team2',
    packages=find_packages(),
    version=version,
    description='Library for preprocessing the data',
    author='remla23_team2',
    license='MIT',
)