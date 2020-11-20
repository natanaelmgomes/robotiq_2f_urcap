# Robotiq 2F-85 (140) gripper ROS package

This package extends the [ROS Industrial Robotiq packages](https://github.com/ros-industrial/robotiq) to connect to the gripper using the original [Robotiq URcap](https://robotiq.com/products/2f85-140-adaptive-robot-gripper) even when the gripper is attached to the [Wrist Camera](https://robotiq.com/products/wrist-camera). The package is written in Python 3.7.

Connect the computer to the UR robot using the ethernet cable and launch the controller.

```
roslaunch robotiq_2f_urcap robotiq_2f_bringup.launch ur_address:=192.168.56.2
```
## References

[Robotiq Community Discussion](https://dof.robotiq.com/discussion/1962/programming-options-ur16e-2f-85)
[Felix von Drigalski code](https://gist.github.com/felixvd/d538cad3150e9cac28dae0a3132701cf)
