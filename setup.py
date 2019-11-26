from setuptools import setup, find_packages

description = """
See `github repo <https://github.com/tempor1s/make-checkin>`_ for information.
"""

VERSION = '2.1.0'

setup(
    name='Make Checkin',
    version=VERSION,
    author='Ben Lafferty',
    author_email='benlaugherty@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ms=src.ms:main']
    },
    description="Suite of tools that makes your MakeSchool life easier!"
)
