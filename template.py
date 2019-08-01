#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Kai Brown
Student Number: BRWKAI001
Prac: Prac 1
Date: 30/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
from itertools import product

# Global Variables


# Logic that you write
def main():
    print("Executing code...press any key to cancel")
    init_GPIO()
    while True:	                              #infinite loop
        GPIO.output(11, not (GPIO.input(11))) #invert LED Output
        GPIO.output(13, not (GPIO.input(13))) #invert LED Output
        GPIO.output(15, not (GPIO.input(15))) #invert LED Output
        time.sleep(1)                         #wait for 1 second

def init_GPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)       #set pin 11 as Out for LED1
    GPIO.setup(13, GPIO.OUT)       #set pin 13 as Out for LED2
    GPIO.setup(15, GPIO.OUT)       #set pin 15 as Out for LED3
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pin 16 as In for SW0 with pull-up
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pin 18 as In for SW1 with pull-up

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
