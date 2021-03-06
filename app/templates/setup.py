#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for Python package.

---
This file is part of pygalle.core.base.klass
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---
"""

import pip
import os, sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.dirname(__file__))

from pygalle_package import CONFIGURATION

links = []
requires = []

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace('\r','') # Do not forget this line
except OSError:
    print('Pandoc not found. Long_description conversion failure.')
    import io
    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

requirements = pip.req.parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=pip.download.PipSession())

download_url = 'https://github.com/<%= github.username %>/<%= github.repository %>/archive/v%s.tar.gz' % CONFIGURATION['version']

for item in requirements:
    # we want to handle package names and also repo urls
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

setup(name='%s' % (CONFIGURATION['name']),
      version=CONFIGURATION['version'],
      description=CONFIGURATION['description'],
      long_description=long_description,
      url='http://github.com/<%= github.username %>/<%= github.repository %>',
      author=CONFIGURATION['author'],
      author_email=CONFIGURATION['email'],
      license=license,
      packages=[os.path.join('src', p) for p in find_packages('src')],
      zip_safe=False,
      install_requires=requires,
      include_package_data=True,
      python_requires=', '.join((
          '>=3.5',
          '!=3.0.*',
          '!=3.1.*',
          '!=3.2.*',
          '!=3.3.*',
      )),
      # extras_require={
      #    'docs': ['Sphinx', 'repoze.sphinx.autointerface'],
      #    'test': tests_require,
      #    'testing': testing_extras,
      # },
      # features=features,
      test_suite='test.test_suite',
      keywords=['pygalle', 'pygalle.io', 'core', 'base', 'class', 'oop', 'microlibrary'],
      classifiers=[
          'Development Status :: 3 - %s' % CONFIGURATION['status'],
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'License :: OSI Approved :: %s License' % CONFIGURATION['license'],
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          ],
      download_url=download_url,
      )
