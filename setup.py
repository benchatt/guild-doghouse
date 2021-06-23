from setuptools import find_packages, setup

setup(
    name='doghouse',
    packages=find_packages(),
    version='0.0.1',
    description='DogHouse Shelter Manager (Guild Interview)',
    author='Ben Chatterton',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest==6.2.4'],
    test_suite='tests',
)
