#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
[tests/stdlib/test_ls.py]

Test the ls command.
"""

import unittest
import os

from ergonomica.ergo import ergo


class TestLs(unittest.TestCase):
    """Tests the `ls` command."""

    def test_ls(self):
        """
        Test the ls function.
        """

        self.assertItemsEqual(ergo('ls'), os.listdir("."))
