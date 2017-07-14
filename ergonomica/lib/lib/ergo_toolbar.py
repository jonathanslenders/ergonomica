#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[lib/lib/toolbar.py]

Defines the "toolbar" command.
"""


import os
import sys


def main(argc):
    """
       toolbar: Set the text for the Ergonomica toolbar (bar at bottom of screen).

       Usage:
          toolbar STRING
    """
    
    argc.env.toolbar = argc.args['STRING']

