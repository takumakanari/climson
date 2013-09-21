from setuptools import setup, find_packages
from climson import (
    __version__,
    __author__,
    __license__,
    __description__
)

setup(
    name = 'climson',
    version = __version__,
    packages = find_packages(
        '.', 
        exclude = [
            '*.tests', '*.tests.*', 'tests.*', 'tests'
        ]
    ),
    package_dir = {
        '' : '.'
    },
    install_requires = [
        'nose'
    ],
    author = __author__,
    author_email = 'chemtrails.t@gmail.com' ,
    url = '',
    description = __description__,
    long_description = open('README.rst').read(),
    keywords = ['unix', 'linux', 'commandline', 'cli', 'command', 'climson'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe = False,
    include_package_data = True
)

