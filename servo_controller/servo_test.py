#!/usr/bin/python
import ServoController as sc

# Set all servo motors to home position
with sc.ServoController() as servo:
    for i in range(0, 18):
        servo.set_angle(i, 90)
