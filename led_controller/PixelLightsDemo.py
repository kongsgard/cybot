#!/usr/bin/env python
# WS2801 pixel control for Raspberry Pi (Requires PixelLights.py)

import time, sys
from PixelLights import PixelLights # Import the Python module (you need to set the number of pixels in here)
LEDs=AndyPiPixelLights() # Set the name of our module
NUMBER_OF_PIXELS=18 # Set the number of pixels
ledpixels = [0] * NUMBER_OF_PIXELS # set up the pixel array


try:
#   LEDs.colorwipe(ledpixels, LEDs.Color(0, 0, 255), 0.05) # wipes blue pixels along the strip

   LEDs.cls(ledpixels) # clears all the pixels to black
   time.sleep(0.5)

 #  LEDs.rainbowCycle(ledpixels, 0.01) # rainbow swirl

  # LEDs.cls(ledpixels) # clears all the pixels to black
  # time.sleep(0.5)


   for i in range(0, 5):
      LEDs.setpixelcolor(ledpixels, i, LEDs.Color(0,255,0)) # from ledpixels, sets pixel 10 (starting from 0) to green
      LEDs.writestrip(ledpixels) # writes the pixels (must be called after setpixelcolor to update
      time.sleep(0.5)


   LEDs.cls(ledpixels) # clears all the pixels to black
   time.sleep(0.5)

except KeyboardInterrupt: # clears all pixels in the case of Ctrl-C exit
   LEDs.cls(ledpixels)
   sys.exit(0)
