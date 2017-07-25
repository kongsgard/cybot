#! /usr/bin/python
import MotorDriver as mc
import time

with mc.MotorDriver() as motor:
    motor.set_speed(0, 1, 100)
    time.sleep(1)
    motor.set_speed(0, 0, 0)
    time.sleep(1)
