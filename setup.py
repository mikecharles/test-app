#!/usr/bin/env python
import sys, os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import pip
from pip.req import parse_requirements


# Get the version
script_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(script_path, 'VERSION')) as version_file:
    version = version_file.read().strip()

# Get requirements
install_reqs = parse_requirements(os.path.join(script_path, 'pip-requirements.txt'), session=False)
install_reqs = [str(ir.req) for ir in install_reqs]

# Create a 'test' subcommand for setup.py
class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# Setup
setup(
    name='python-skeleton',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='CC',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    ],
    entry_points={
        'console_scripts': [
            'python-skeleton = python_skeleton.__main__:main'
        ]
    },
    install_requires=install_reqs,
    tests_require=['pytest'],
    cmdclass={
        'test': PyTest,
    },

)
