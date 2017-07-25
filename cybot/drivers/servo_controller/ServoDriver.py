import serial

class ServoDriver:
    device = '/dev/ttyACM0'
    baud_rate = 9600
    timeout = 1

    min_angle = 0.0
    max_angle = 180.0
    min_target = 256.0
    max_target = 13120.0

    def __init__(self):
        self.ser = serial.Serial(self.device, self.baud_rate, timeout = self.timeout)

    def __enter__(self):
        return self

    def set_angle(self, channel, angle):
        scaled_angle = self.get_scaled_angle(angle)

        command_byte = chr(0x84)
        channel_byte = chr(channel)

        low_target_byte = chr(scaled_angle & 0x7F)
        high_target_byte = chr((scaled_angle >> 7) & 0x7F)

        command = command_byte + channel_byte + low_target_byte + high_target_byte
        self.ser.write(command)
        self.ser.flush()

    def get_scaled_angle(self, angle):
        return int((angle / ((self.max_angle - self.min_angle) /
               (self.max_target - self.min_target))) + self.min_target)

    def __exit__(self, exc_type, exc_value, traceback):
        self.ser.close()
