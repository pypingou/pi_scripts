#!/usr/bin/python

"""
This script simply makes a LED blink.

The important factor being the ``pin`` variable refering to the GPIO identifier.
For my set-up, the identifier ``21`` refers to the output P02.

If you need help to find which is which, see the `iterate_gpio_led` script.
"""


import RPi.GPIO as GPIO
import time

pin = 21

# numbering scheme that corresponds to breakout board and pin layout
GPIO.setmode(GPIO.BCM)

# Set up on which pin to activate
GPIO.setup(pin, GPIO.OUT)
while True:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)


