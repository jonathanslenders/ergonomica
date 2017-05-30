#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[lib/lib/ergo_pyvim.py]

Defines the "pyvim" command.
"""

from __future__ import unicode_literals
from pyvim.entry_points.run_pyvim import run


def main(argc):
    """
    pyvim: Pure Python Vim clone.

    Usage:
       pyvim [FILES...]
    """

    # seems extraneous
    # pylint: disable=too-many-function-args
    run(argc.args['FILES'])
