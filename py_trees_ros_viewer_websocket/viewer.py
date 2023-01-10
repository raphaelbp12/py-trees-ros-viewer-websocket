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
A qt-javascript application for viewing executing or replaying py_trees
"""
##############################################################################
# Imports
##############################################################################


import threading

import rclpy
import math

from . import backend as ros_backend
from . import console

##############################################################################
# Main
##############################################################################


def main():
    # logging
    console.log_level = console.LogLevel.DEBUG

    # ros init
    rclpy.init()

    # the players
    snapshot_period = math.inf
    backend = ros_backend.Backend(
        parameters=ros_backend.SnapshotStream.Parameters(
            blackboard_data=True,
            blackboard_activity=True,
            snapshot_period=snapshot_period)
    )

    # backend.discovered_namespaces_changed.connect(window.on_discovered_namespaces_changed)
    # backend.tree_snapshot_arrived.connect(window.on_tree_snapshot_arrived)

    # qt/ros bringup
    ros_thread = threading.Thread(target=backend.spin)
    ros_thread.start()

    # shutdown
    backend.node.get_logger().info("waiting for backend to terminate [viewer]")
    ros_thread.join()
    rclpy.shutdown()
