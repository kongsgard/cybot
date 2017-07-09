#! /usr/bin/python
import MotorController as mc
import time

with mc.MotorController() as motor:
    motor.set_speed(0, 1, 100)
    time.sleep(1)
    motor.set_speed(0, 0, 0)
    time.sleep(1)
