#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: BSD
#   https://github.com/splintered-reality/py_trees_ros_viewer/raw/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Utilities for the py_trees ros viewer.
"""
##############################################################################
# Imports
##############################################################################

import rclpy.qos

##############################################################################
# Symbols
##############################################################################


class XhtmlSymbols(object):

    def __init__(self):
        self.space = '<text>&#xa0;</text>'
        self.left_arrow = '<text>&#x2190;</text>'
        self.right_arrow = '<text>&#x2192;</text>'
        self.left_right_arrow = '<text>&#x2194;</text>'
        self.bold = '<b>'
        self.bold_reset = '</b>'
        self.reset = '</text>'
        self.normal = '<text>'
        self.cyan = '<text style=[doubleQuote]color:cyan;[doubleQuote]>'
        self.green = '<text style=[doubleQuote]color:green;[doubleQuote]>'
        self.yellow = '<text style=[doubleQuote]color:darkgoldenrod;[doubleQuote]>'
        self.red = '<text style=[doubleQuote]color:red;[doubleQuote]>'
        self.monospace = '<text style=[doubleQuote]font-family: monospace;[doubleQuote]>'
        self.multiplication_x = '<text>&#x2715;</text>'
        self.forbidden_circle = '<text>&#x29B8;</text>'

##############################################################################
# Methods
##############################################################################


def parent_namespace(
    name: str
):
    """
    Get the parent namespace of this ros name.
    """
    return "/".join(name.split("/")[:-1])


def qos_profile_latched() -> rclpy.qos.QoSProfile:
    """
    Convenience retrieval for a latched topic (publisher / subscriber)
    """
    return rclpy.qos.QoSProfile(
        history=rclpy.qos.QoSHistoryPolicy.KEEP_LAST,
        depth=1,
        durability=rclpy.qos.QoSDurabilityPolicy.TRANSIENT_LOCAL,
        reliability=rclpy.qos.QoSReliabilityPolicy.RELIABLE
    )


def normalise_name_strings(name) -> str:
    """
    To prepare them for a json dump, they need to have newlines and
    superflous apostrophe's removed.

    Args:
        name: name to normalise
    """
    return name.replace("'", ' ').replace('"', ' ').replace('\n', ' ')
