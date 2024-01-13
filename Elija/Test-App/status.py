#!/usr/bin/python3
#
# Example script from
#     https://electrosome.com/using-switch-raspberry-pi/
#
import RPi.GPIO as GPIO          #Import GPIO library
import time

GPIO.setmode(GPIO.BOARD)         #Set GPIO pin numbering
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Enable input and pull up resistors
input_state = GPIO.input(12) #Read and store value of input to a variable

if input_state == False:     #Check whether pin is grounded
    print('Button on')  #Print 'Button Pressed'
    exit(0)
else:
    print("Button off")
    exit(1)

