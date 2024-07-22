import constants as const
import gc
import math
import time

from hexapod import Hexapod
from leg import Leg
from plasma import WS2812
from servo import servo2040

def setUpLEDs():
    led_bar = WS2812(servo2040.NUM_LEDS, 1, 0, servo2040.LED_DATA)
    led_bar.start()
    offset = 0.0

    for i in range(servo2040.NUM_LEDS):
        hue = float(i) / servo2040.NUM_LEDS
        led_bar.set_hsv(i, hue + offset, 1.0, const.BRIGHTNESS)

def main():
    print("Start Program")
    setUpLEDs()
    hexapod = Hexapod()
    hexapod.moveAllToHome()
    time.sleep(1)
    
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exit Program")
        for leg in hexapod.legs.values():
            leg.disableServos()

if __name__ == "__main__":
    main()