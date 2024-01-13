#!/usr/bin/python3
#
# Example script from
#     https://electrosome.com/using-switch-raspberry-pi/
#
import RPi.GPIO as GPIO          #Import GPIO library
import time                      #Import time library
GPIO.setmode(GPIO.BOARD)         #Set GPIO pin numbering
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Enable input and pull up resistors
while True:
    input_state = GPIO.input(12) #Read and store value of input to a variable
    if input_state == False:     #Check whether pin is grounded
        print('Button Pressed')  #Print 'Button Pressed'
        time.sleep(0.3)          #Delay of 0.3s
