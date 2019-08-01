#!/usr/bin/python3
"""
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
LED_Lib = list(product((0,1),(0,1),(0,1)))	#List of 3 bit binary numbers equal to index
LED_Lst = [11, 13, 15]				#Pin addresses of LEDs
Count = 0					#Counter for LEDs

# Function Definitions
def main():
    print("Executing code...press any key to cancel")
    init_GPIO()
    while True:	                              #infinite loop
        time.sleep(10)                         #wait for 10 seconds each iteration

def init_GPIO():
    global LED_Lst
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_Lst, GPIO.OUT)       #set pins 11, 13, 15 for LED0-2
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pin 16 as In for SW0 with pull-up
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pin 18 as In for SW1 with pull-up
    GPIO.add_event_detect(16, GPIO.RISING, callback=Increase, bouncetime=200)  # add rising edge detection on SW0 for Increase
    GPIO.add_event_detect(18, GPIO.RISING, callback=Decrease, bouncetime=200)  # add rising edge detection on SW1 for Decrease

def Increase(channel):                       #SW0 pressed, Increase LEDs
    global LED_Lib
    global LED_Lst
    global Count
    if Count == 7:                      #If 8: Overflow to 0
        Count = 0
    else:                               #Else: Increment LEDs
        Count +=1
    GPIO.output(LED_Lst,LED_Lib[Count]) #Update LEDs

def Decrease(channel):                       #SW1 pressed, decrease LEDs
    global LED_Lib
    global LED_Lst
    global Count
    if Count == 0:                      #If 0: Overflow to 8
        Count = 7
    else:                               #Else: Decrement LEDs
        Count -=1
    GPIO.output(LED_Lst,LED_Lib[Count]) #Update LEDs

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
