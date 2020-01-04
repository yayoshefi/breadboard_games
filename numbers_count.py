#!/usr/bin/python3.5

numbers = {
    0: '/home/pi/Music/numbers/AUD-20190506-WA0012.mp3',
    1: '/home/pi/Music/numbers/AUD-20190506-WA0002.mp3',
    2: '/home/pi/Music/numbers/AUD-20190506-WA0003.mp3',
    3: '/home/pi/Music/numbers/AUD-20190506-WA0004.mp3',
    4: '/home/pi/Music/numbers/AUD-20190506-WA0005.mp3',
    5: '/home/pi/Music/numbers/AUD-20190506-WA0006.mp3',
    6: '/home/pi/Music/numbers/AUD-20190506-WA0007.mp3',
    7: '/home/pi/Music/numbers/AUD-20190506-WA0008.mp3',
    8: '/home/pi/Music/numbers/AUD-20190506-WA0009.mp3',
    9: '/home/pi/Music/numbers/AUD-20190506-WA0010.mp3',
    10: '/home/pi/Music/numbers/AUD-20190506-WA0011.mp3'
    }

    
from gpiozero import LED, Button
conter_btn = Button(16) # TODO Choose button

import pygame
pygame.mixer.init()
player = pygame.mixer.music


# start the luma led 32*8 led matrix
from breadboard.luma_local_utils import set_serial, set_long_device
serial = set_serial()
cntr = 0

def activate(num):
    device = set_long_device()
    global cntr
    from luma.core.render import canvas
    from luma.core.legacy import text, show_message
    from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
    player.load(numbers[num])
    player.play()
    if cntr == 10:
        show_message(device, '10', fill="white", font=proportional(CP437_FONT),
        scroll_delay=0.08)
    else:
        with canvas(device) as draw:
            text(draw, (0, 0), str(num), fill="white", font=proportional(CP437_FONT))

    cntr = (cntr+1) % 11
    import time
    while player.get_busy():
        time.sleep(0.1)
    

def cleanup ():
    import sys
    from luma.led_matrix.device import max7219
    from luma.core.legacy import text, show_message
    device = set_long_device()
    show_message(device, 'Shutting down', fill='white', scroll_delay=0.05)
    sys.exit (0)



def run():
    print ("Ready to Count?")
    from luma.led_matrix.device import max7219
    from luma.core.legacy import text, show_message
    device = set_long_device()
    show_message(device, 'Ready to count?', fill='white', scroll_delay=0.05)
    while True:
        conter_btn.when_pressed = lambda: activate(cntr)
        #counter_btn.when_held = cleanup()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Maya's Counting numbers game")
    parser.add_argument('--debug', dest='debug', action='store_true',
                        default=False, help='debugger mode- no need to press the button')
    args = parser.parse_args()

    run()
    #for _ in range(10):
    #    activate(cntr)
    
