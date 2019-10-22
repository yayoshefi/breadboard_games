#! /usr/bin/python3

from gpiozero import LED, Button
from signal import pause

led    = LED(17)
button = Button(2)

if __name__ == '__main__':
    print ("Starting Maya's LED Game - press to light")
    button.when_pressed  = led.on
    button.when_released = led.off

    pause ()
