# PyTrees Ros Viewer Websocket

## About

ROS2 Node - py_trees tooling - A modified version of py_trees_ros_viewer (by Daniel Stonier). That publish the parsed tree data to a new topic. In order to serve with Rosbridge Websocket.
[ROS2 PyTrees](https://github.com/splintered-reality/py_trees_ros#pytrees-ros-ecosystem).

This code was totally based on `py_trees_ros_viewer`
[PyTrees Ros Viewer](https://github.com/splintered-reality/py_trees_ros_viewer).

## Disclaimer

This node was rushed in order to make a delivery within a deadline, feel free to improve it with a pull request! :)

It is important that you read all the info section (it is quite short).

## Info

This node expects that you know the your's tree node name. The default case is: `tree`.

You can change it in `backend.py` at `line 261`.

This variable will be used watch the node list and reset the connection if your tree was reseted.

When running, it will publish the parsed data in a topic called `/tree_js_parsed_data` with a `String` type.

In order to parse it correctly in a JSON form, you need to replace the `[doubleQuote]` to `"`.

## Quickstart

You should clone this repo and build it:

```
colcon build --symlink-install
```

Then, source it:

```
source install/setup.bash
```

Now, you can run it:

```
py-trees-tree-viewer-websocket
```

```
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```
