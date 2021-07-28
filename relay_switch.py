#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import logging
import sys

# Function to turn a relay on with logging
def relay_on():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_CONTROL, GPIO.OUT)
    GPIO.output(GPIO_CONTROL, False)

    logging.basicConfig(format='%(asctime)s %(message)s', filename='/home/pi/Do$
    logging.info('Relay has been manually switched on, from relay_on_off.py')

# Function to turn relay off with logging
def relay_off():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_CONTROL, GPIO.OUT)
    GPIO.output(GPIO_CONTROL, True)

    logging.basicConfig(format='%(asctime)s %(message)s', filename='/home/pi/Do$
    logging.info('Relay has been manually switched off, from relay_on_off.py')

def main():
    # Evaluate user input on script run (either 'on' of 'off')
    while True:
        if data == 'on':
            relay_on()
            break
        elif data == 'off':
            relay_off()
            break

# Basic function run with user input after script call
if __name__ == "__main__":
    GPIO.setwarnings(False)
    data = sys.argv[1]
    global GPIO_CONTROL
    GPIO_CONTROL = 23
    main()



