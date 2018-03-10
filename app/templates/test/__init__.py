#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---
This file is part of <%= name %>
Copyright (c) <%= year %> <%= author.name %>.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---
"""

import unittest
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('test', pattern='test_*.py')
    print(test_suite)
    return test_suite
