import serial

class MotorDriver:
    device = '/dev/ttyUSB0'
    baud_rate = 19200
    timeout = 1

    def __init__(self):
        self.ser = serial.Serial(self.device, self.baud_rate, timeout = self.timeout)

    def __enter__(self):
        return self

    def set_speed(self, motor, direction, speed):
        if motor == 0 and direction == 0:
            send_byte = chr(0xC2)
        if motor == 1 and direction == 0:
            send_byte = chr(0xCA)
        if motor == 0 and direction == 1:
            send_byte = chr(0xC1)
        if motor == 1 and direction == 1:
            send_byte = chr(0xC9)
        self.ser.write(send_byte)
        self.ser.write(chr(speed))

    def __exit__(self, exc_type, exc_value, traceback):
        self.ser.close()
