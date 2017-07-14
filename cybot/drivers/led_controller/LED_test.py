#!/usr/bin/env python
import sys
import time
from LEDController import LEDController

LEDs = LEDController()

LED_command = ''
if len(sys.argv) > 1:
    LED_command = sys.argv[1]

try:
    if LED_command = 'color_wipe':
        LEDs.color_wipe(LEDs.color(0, 0, 255), 0.0) # Blue color wipe
    elif LED_command == 'rainbow_cycle'
        LEDs.rainbow_cycle(0.00)
    else:
        LEDs.set_all_pixels(0, 0, 255) # Blue color
    LEDs.clear()
except KeyboardInterrupt:
    LEDs.clear()
    sys.exit(0)
