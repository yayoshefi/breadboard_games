#! /usr/bin/python3

from gpiozero import LED, Button
# import pygame.mixer
# from pygame.mixer import Sound
# from signal import pause
# import random

from omxplayer.player import OMXPlayer
# import subprocess
import time
import argparse
import sys

parser = argparse.ArgumentParser(description="Maya's playlist app.")
parser.add_argument('--debug', dest='debug', action='store_true',
                    default=False, help='debugger mode- no need to press the button')
parser.add_argument('--output', dest='output', action='store',
                    default=None, help='use alsa / hdmi / analog / both for output select')

args = parser.parse_args()

player_args = []
player_args = ['-o', args.output] if args.output else []

led        = LED(17)
white_btn  = Button(2)
red_btn    = Button(22)
yellow_btn = Button(5)
blue_btn   = Button(26)

music_dir = '/home/pi/Music/'
lvl       = 3
songs = {  # songs list
    1: music_dir+"run_my_horse.mp3"      ,
    2: music_dir+"lady_with_baskets.mp3" ,
    3: music_dir+"i_have_an_icecream.mp3",
    4: music_dir+"little_yonatan.mp3"    ,
    5: music_dir+"mi_yemalel.mp3"        ,
    6: music_dir+"hanuka_long.mp3"       ,
    7: music_dir+"lullabye_in_ragtime.mp3",
    8: music_dir+"shabat_baboker.mp3",
    9: music_dir+"kol_od.mp3",
    10: music_dir+"meeting_till_the_end.mp3",
    }

# Start player with default song = RUTZ BEN SUSI
player = OMXPlayer(songs[1], args=player_args, pause=True)


# THIS DICT IS SET TO BE ABLE TO WORK WITH MULTIPLE BUTTONS
# button_sounds = {
#   Button(2): player.load(songs[1]),
# }
# for button, sound in button.sounds.items():
#   button.when_pressed = sound.play

def quit_maya():
    print("SHEFI - ONLY ONE BUTTON IS PRESSED,\n\tPRESS SECOND WHITE BUTTON TO QUIT")
    if blue_btn.is_held and white_btn.is_held:
        print("SHEFI BOTH WHITE BUTTONS ARE HELD")
        print("SHEFI:",time.asctime() ,"Bye Bye")
        sys.exit(0)  # WHY THIS DOESNOT WORK?! - maybe because it's not an executable?
    elif blue_btn.is_held: print("only blue is held")
    elif white_btn.is_held: print("only white is held")


def debug_songs(song=1):
    print(["SHEFI testing func", str(song)])


def play_omx(song=1):
    """ 
    play_omx function is the basic function to load a new song and play it
    defulut song is ROTZ BEN SUSI 
    """
    player.load(songs[song])
    if song in [7]:  #lullabye in ragtime is a bit low volume
        player.set_volume(4)
    else:
        player.set_volume(1)

#    song_time = player.duration()
    print("PLAYING "+songs[song].split('/')[-1])
    led.blink(on_time=1.5,n=5)


if __name__ == '__main__':
    if args.debug:
        play_omx()
    else:
        print("Starting Maya's Press To Play Game")
        white_btn.when_pressed = lambda: play_omx(song=1)
#        white_btn.when_pressed += debug_songs  # this should also print the debug message in addition to the play song
        red_btn.when_pressed = lambda: play_omx(song=8)
        yellow_btn.when_pressed = lambda: play_omx(song=9)
        blue_btn.when_pressed = lambda: play_omx(song=10)

        white_btn.when_held = quit_maya
        blue_btn.when_held  = quit_maya

        #player.playEvent = lambda: led.blink(n=4)

        while True:
            if blue_btn.is_held and white_btn.is_held:
                print("Bye Bye Maya")
                sys.exit(0)
#        #pause()


# TRUNK
# FIXME - set the sys.exit to work also using the when_held event callback
# TODO - connect two function to the event handler
