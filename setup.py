#!/usr/bin/env python
     
from setuptools import setup, find_packages

setup(name='pyfnordmetric',
    version='0.0.1',
    description='A Python client for fnordmetric',
    author='Stephen Holiday',
    author_email='stephen.holiday@gmail.com',
    url='https://github.com/sholiday/pyfnordmetric',
    py_modules=['fnordmetric'],
    install_requires=(
        'redis',
    ),
   },
   classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: Apache Software License',
         'Operating System :: MacOS :: MacOS X',
         'Operating System :: POSIX',
         'Operating System :: Unix',
         'Programming Language :: Python :: 2.6',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python',
         'Topic :: System :: Monitoring',
   ],
   download_url="https://github.com/sholiday/pyfnordmetric/tarball/master",
   long_description = """
   A client for fnordmetric
   """
)