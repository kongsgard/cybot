#!/usr/bin/env python
# WS2801 pixel control for Raspberry Pi (Requires PixelLights.py)

import sys
import time
from PixelLights import PixelLights

LEDs = PixelLights() # Set the name of our module
NUMBER_OF_PIXELS = 160 # Set the number of pixels
led_pixels = [0] * NUMBER_OF_PIXELS # set up the pixel array

try:
    # LEDs.color_wipe(led_pixels, LEDs.color(0, 0, 255), 0.05) # wipes blue pixels along the strip

    LEDs.clear(led_pixels) # clears all the pixels to black
    time.sleep(0.5)

    # LEDs.rainbow_cycle(led_pixels, 0.01) # rainbow swirl

    # LEDs.clear(led_pixels) # clears all the pixels to black
    # time.sleep(0.5)

    for i in range(0, 5):
        LEDs.set_pixel_color(led_pixels, i, LEDs.color(0,255,0)) # from ledpixels, sets pixel 10 (starting from 0) to green
        LEDs.write_strip(led_pixels) # writes the pixels (must be called after setpixelcolor to update
        time.sleep(0.5)

    LEDs.clear(led_pixels) # clears all the pixels to black
    time.sleep(0.5)

except KeyboardInterrupt: # clears all pixels in the case of Ctrl-C exit
    LEDs.clear(led_pixels)
    sys.exit(0)
