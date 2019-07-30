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

# Logic that you write
def main():
    print("Executing code...press any key to cancel")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)       #set pin 7 as Out for LED
    while True:	                  #infinite loop
        GPIO.output(7, not GPIO.input(7)) #sets the value of Pin 7 (GPIO 4) high
        time.sleep(1)          #wait for 1? second


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
