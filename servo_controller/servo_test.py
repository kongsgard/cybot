#!/usr/bin/python
import ServoController as sc
import sys

# Set all servo motors to home position
with sc.ServoController() as servo:
    for i in range(0, 18):
        servo.set_angle(i, int(sys.argv[1]))
