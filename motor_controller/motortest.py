#! /usr/bin/python
import serial
import time
def setSpeed(ser, motor, direction, speed):
    if motor == 0 and direction == 0:
        sendByte = chr(0xC2)
    if motor == 1 and direction == 0:
        sendByte = chr(0xCA)
    if motor == 0 and direction == 1:
        sendByte = chr(0xC1)
    if motor == 1 and direction == 1:
        sendByte = chr(0xC9)
    ser.write(sendByte)
    ser.write(chr(speed))

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout = 1)

setSpeed(ser, 0 , 1 , 100)
setSpeed(ser, 1 , 1 , 100)
time.sleep(1)
setSpeed(ser, 0 , 0 , 0)
setSpeed(ser, 1 , 0 , 0)
time.sleep(1)
ser.close()
