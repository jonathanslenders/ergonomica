#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
[tests/stdlib/test_cp.py]

Tests the cp command.
"""

import os
import unittest
from ergonomica import ergo

class TestMkdir(unittest.TestCase):
    """Tests the mkdir command."""

    def test_mkdir(self):
        """
        Tests the mkdir command.
        """

        self.assertFalse(os.path.isdir("test_mkdir"))
        ergo("mkdir test_mkdir")
        self.assertTrue(os.path.isdir("test_mkdir"))
        os.rmdir("test_mkdir")

