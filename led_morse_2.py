#!/usr/bin/python

"""
This script allows to do morse code using two LED one for the . and one
one for the -

The important factor being the ``pin`` variable refering to the GPIO identifier.
For my set-up, the identifier ``21`` refers to the output P02 and the
identifier ``24`` refers to the output P05.

If you need help to find which is which, see the `iterate_gpio_led` script.
"""


import sys
import time
import RPi.GPIO as GPIO

PIN = 21
PIN2 = 24


MORSE_CODE = {
    ' ': ' ',
    "'": '.----.',
    '(': '-.--.-',
    ')': '-.--.-',
    ',': '--..--',
    '-': '-....-',
    '.': '.-.-.-',
    '/': '-..-.',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ':': '---...',
    ';': '-.-.-.',
    '?': '..--..',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--.-'
}


def blink_morse(text, pin, pin2):
    """ For a given text, set-up the pi to blink and encode the text in
    morse code.
    """
    # numbering scheme that corresponds to breakout board and pin layout
    GPIO.setmode(GPIO.BCM)
    # Set up on which pin to activate
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    for letter in text:
        code = MORSE_CODE[letter.upper()]
        print letter, code
        for char in code:
            GPIO.output(pin, GPIO.HIGH)
            GPIO.output(pin2, GPIO.HIGH)
            time.sleep(0.5)
            if char == '.':
                GPIO.output(pin, GPIO.LOW)
                time.sleep(0.5)
            elif char == '-':
                GPIO.output(pin2, GPIO.LOW)
                time.sleep(1)
            else:
                time.sleep(0.5)


def main():
    """ Main function, ensure there is something to blink and if so blink
    it.
    """
    if len(sys.argv) < 2:
        print 'USAGE: led_morse.py text to blink in morse code'
        return 1

    text = ' '.join(sys.argv[1:])
    blink_morse(text, PIN, PIN2)


if __name__ == '__main__':
    sys.exit(main())
