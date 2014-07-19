#!/usr/bin/python

"""
The goal of this script is to iterate over the different GPIO output and find
which one corresponds to which python GPIO identifier.

For example, on my breadboard, the output named ``P01`` corresponds to the GPIO
identifier ``21``.

So to find out which is which, I simply connect a LED and iterate over the
different GPIO output.

.. note:: The GPIO identifier #6 is skipped, it corresponds to the ground output
          and if called it pretty much crash the pi.

"""

import RPi.GPIO as GPIO
import time

# numbering scheme that corresponds to breakout board and pin layout
GPIO.setmode(GPIO.BCM)

def blink(pin):
    print pin
    # Set up on which pin to activate
    GPIO.setup(pin, GPIO.OUT)
    cnt = 0
    while cnt < 3:
        cnt += 1
#        print '  high' 
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)
#        print '  low' 
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)

# 6 is ground
for i in [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26]:
    blink(i)

