#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---
This file is part of azimutt-metrics-collector
Copyright (c) 2020 Azimutt Team.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---
"""

import unittest
import inspect
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join('..','src')))

from azimutt-metrics-collector import KlassExample


class ExampleTest(unittest.TestCase):
    """ Unit tests for PygalleBaseClassTest.
    """

    def test_isclass(self):
        """ Is {PygalleBaseClass} really a class ? """
        self.assertEqual(inspect.isclass(PygalleBaseClass), True)

    def test_create_instance(self):
        """ Create a new instance of {PygalleBaseClass} """
        self.assertIsInstance(PygalleBaseClass(), PygalleBaseClass)

def main():
    """ Entry point.
    """
    unittest.main()

if __name__ == '__main__':
    main()

