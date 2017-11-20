#!/usr/bin/env python

from distutils.core import setup

setup(name="tastemakers",
      version="0.1.5",
      classifiers = ['Environment :: Console',
                     'Intended Audience :: System Administrators',
                     'License :: Other/Proprietary License',
                     'Natural Language :: English',
                     'Operating System :: POSIX',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.4',
                     'Programming Language :: Python :: 2.5',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                     'Topic :: System :: Monitoring',
                     'Topic :: Database',
                     'Topic :: Database :: Database Engines/Servers',
                     ],
      description="Python Client for Tastemakers Africa Platform",
      author="Tastemakers Africa",
      author_email="support@tastemakersafrica.com",
      url="https://github.com/TSTMKRSAfrica/Tastemakers-Python-SDK",
      packages=["tastemakers"],
      install_requires=["requests"],
      tests_require=["nose"]
)