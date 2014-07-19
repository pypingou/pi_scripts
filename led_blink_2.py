#!/usr/bin/python

"""
This script makes two LEDs blink at opposite rythms.

The important factors are the ``pin`` and ``pin2`` variables refering to the
GPIO identifiers.
For my set-up, the identifier ``21`` refers to the output P02 and the identifier
``24`` referes to the output P05.

If you need help to find which is which, see the `iterate_gpio_led` script.
"""



import RPi.GPIO as GPIO
import time

pin = 21
pin2 = 24

# numbering scheme that corresponds to breakout board and pin layout
GPIO.setmode(GPIO.BCM)

# Set up on which pin to activate
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
while True:
    GPIO.output(pin, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    time.sleep(0.5)


