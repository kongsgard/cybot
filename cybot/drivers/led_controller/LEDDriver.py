#!/usr/bin/env python
# WS2801 SPI control class for Raspberry Pi

import RPi.GPIO as GPIO, time, os, sys

class LEDDriver:
    led_pixels = [0] * 160 # Number of pixels in LED strip

    GPIO.setmode(GPIO.BCM)
    SPICLK = 23 # The SPI clock pin on the Raspberry Pi
    SPIDO = 19 # The SPI data line (MOSI) on the Raspberry Pi

    def slow_spi_write(self, clockpin, datapin, byteout):
        GPIO.setup(clockpin, GPIO.OUT)
        GPIO.setup(datapin, GPIO.OUT)
        for i in range(8):
            if (byteout & 0x80):
                GPIO.output(datapin, True)
            else:
                GPIO.output(clockpin, False)
            byteout <<= 1
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)

    def write_strip(self):
        spidev = file("/dev/spidev0.0", "w")
        for pixel in range(len(self.led_pixels)):
            spidev.write(chr((self.led_pixels[pixel]>>16) & 0xFF))
            spidev.write(chr((self.led_pixels[pixel]>>8) & 0xFF))
            spidev.write(chr(self.led_pixels[pixel] & 0xFF))
        spidev.close()
        time.sleep(0.002)

    def color(self, r, g, b):
        return ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)

    def set_pixel_color(self, pixel, r, g, b):
        if (pixel >= len(self.led_pixels)):
            return
        self.led_pixels[pixel] = self.color(r, g, b)

    def set_pixel_color(self, pixel, color):
        if (pixel >= len(self.led_pixels)):
            return
        self.led_pixels[pixel] = color

    def color_wipe(self, color, delay):
        for pixel in range(len(self.led_pixels)):
            self.set_pixel_color(pixel, color)
            self.write_strip()
            time.sleep(delay)

    def wheel(self, wheel_pos):
        if (wheel_pos < 85):
            return self.color(wheel_pos * 3, 255 - wheel_pos * 3, 0)
        elif (wheel_pos < 170):
            wheel_pos -= 85;
            return self.color(255 - wheel_pos * 3, 0, wheel_pos * 3)
        else:
            wheel_pos -= 170;
            return self.color(0, wheel_pos * 3, 255 - wheel_pos * 3)

    def rainbow_cycle(self, wait):
        for color in range(256): # One cycle of all 256 colors in the wheel
            for pixel in range(len(self.led_pixels)):
                self.set_pixel_color(pixel, self.wheel( ((pixel * 256 / len(self.led_pixels)) + color) % 256) )
            self.write_strip()
            time.sleep(wait)

    def clear(self):
        for pixel in range(len(self.led_pixels)):
            self.set_pixel_color(pixel, self.color(0, 0, 0))
        self.write_strip()
