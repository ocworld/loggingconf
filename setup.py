# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import io

with io.open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

with io.open('LICENSE', mode='r', encoding='utf-8') as f:
    license_text = f.read()

setup(
    name='loggingconf',
    version='1.0',
    description='Helper library for logging module loading a config file',
    long_description=readme,
    author='Keunhyun Oh',
    author_email='ocworld@gmail.com',
    url='https://github.com/ocworld/loggingconf',
    license=license_text,
    packages=find_packages(exclude=('tests', 'docs')),
    platforms=['any'],
    install_requires=['PyYAML>=5.1'],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    classifiers={
        'Programming Language :: Python',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    },
    project_url={
        'Bug Reports': 'https://github.com/ocworld/loggingconf/issues',
        'Source': 'https://github.com/ocworld/loggingconf'
    }
)
