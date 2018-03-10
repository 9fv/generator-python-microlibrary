#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---
This file is part of pygalle.core.base.error
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---
"""

from pynt import task
import yaml
import os, sys
from pygit2 import Repository

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..','src')))

import <%= name %> as kls

configuration_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yml')
travis_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.travis.yml')
CONFIGURATION = yaml.load(open(configuration_filename, 'r'))
CONFIGURATION['pythons'] = yaml.load(open(travis_filename, 'r'))['python']
CONFIGURATION['github']['branch'] = Repository('.').head.shorthand
CONFIGURATION['package']['description'] = kls.__description__
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'README.md')

from jinja2 import Environment, FileSystemLoader


@task()
def clean():
    '''Clean build directory.'''
    print('Cleaning build directory...')

@task(clean)
def readme():
    """ Generate README.md from templates. """
    print('Generating README')
    env = Environment(loader=FileSystemLoader('.templates'))
    template = env.get_template('README.md.jinja')
    output_from_parsed_template = template.render(CONFIGURATION)
    f = open(README, 'w')
    f.write(output_from_parsed_template)
    f.close()

@task(readme)
def docs():
    print('Generating documentation')
