#!/usr/bin/env python3

import blinkt
import math
import time

def color(deg):
    rad = (deg / 180.0) * math.pi
    return int(127 * (1. + math.sin(rad)))

def show():
    for deg in range(0, 360 * 5, 30):
        for i in range(8):
            r = color(deg + i * 35 + 0)
            g = color(deg + i * 35 + 120)
            b = color(deg + i * 35 + 240)
            blinkt.set_pixel(i, r, g, b)
        blinkt.show()
        time.sleep(.01)
    blinkt.clear()
    blinkt.show()

if __name__ == '__main__':
    show()
