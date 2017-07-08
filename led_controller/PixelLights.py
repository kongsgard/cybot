#!/usr/bin/env python
# WS2801 SPI control class for Raspberry Pi

import RPi.GPIO as GPIO, time, os, sys

class PixelLights:
    NUMBER_OF_PIXELS = 160 # Number of pixels in LED strip
    DEBUG = 1
    GPIO.setmode(GPIO.BCM)
    SPICLK = 23 # The SPI clock pin on the Raspberry Pi
    SPIDO = 19 # The SPI data line (MOSI) on the Raspberry Pi
    led_pixels = [0] * NUMBER_OF_PIXELS

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

    def write_strip(self, pixels):
        spidev = file("/dev/spidev0.0", "w")
        for i in range(len(pixels)):
            spidev.write(chr((pixels[i]>>16) & 0xFF))
            spidev.write(chr((pixels[i]>>8) & 0xFF))
            spidev.write(chr(pixels[i] & 0xFF))
        spidev.close()
        time.sleep(0.002)

    def color(self, r, g, b):
        return ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)

    def set_pixel_color(self, pixels, n, r, g, b):
        if (n >= len(pixels)):
            return
        pixels[n] = self.color(r,g,b)

    def set_pixel_color(self, pixels, n, c):
        if (n >= len(pixels)):
            return
        pixels[n] = c

    def color_wipe(self, pixels, c, delay):
        for i in range(len(pixels)):
            self.set_pixel_color(pixels, i, c)
            self.write_strip(pixels)
            time.sleep(delay)

    def wheel(self, wheel_pos):
        if (wheel_pos < 85):
            return self.color(wheel_pos * 3, 255 - wheel_pos * 3, 0)
        elif (wheelPos < 170):
            wheel_pos -= 85;
            return self.Color(255 - wheel_pos * 3, 0, wheel_pos * 3)
        else:
            wheel_pos -= 170;
            return self.Color(0, wheel_pos * 3, 255 - wheel_pos * 3)

    def rainbow_cycle(self, pixels, wait):
        for color in range(256): # one cycle of all 256 colors in the wheel
            for pixel in range(len(pixels)):
                # tricky math! we use each pixel as a fraction of the full 96-color wheel
                # (thats the i / strip.numPixels() part)
                # Then add in j which makes the colors go around per pixel
                # the % 96 is to make the wheel cycle around
                self.set_pixel_color(pixels, pixel, self.wheel( ((pixel * 256 / len(pixels)) + color) % 256) )
            self.write_strip(pixels)
            time.sleep(wait)

    def clear(self, pixels):
        for i in range(len(pixels)):
            self.set_pixel_color(pixels, i, self.color(0,0,0))
            self.write_strip(pixels)

    def main(self):
        try:
            self.color_wipe(self.led_pixels, self.color(255, 0, 0), 0.05)
            self.color_wipe(self.led_pixels, self.color(0, 255, 0), 0.05)
            self.color_wipe(self.led_pixels, self.color(0, 0, 255), 0.05)
            self.rainbow_cycle(self.led_pixels, 0.00)
            self.clear(self.led_pixels)
        except KeyboardInterrupt:
            self.cls(self.led_pixels)
            sys.exit(0)

if  __name__ == '__main__':
    LEDs = PixelLights()
    LEDs.main()
