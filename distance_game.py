#!/usr/bin/python3

from breadboard import distance_meassure as dst
import time

COMMANDS = {
    'get_closer': '/home/pi/Music/distance_game_mp4/get_closer.mp3',
    'get_far': '/home/pi/Music/distance_game_mp4/get_far.mp3',
    'game_begin': '/home/pi/Music/distance_game_mp4/game_begin.mp3',
    'found': '/home/pi/Music/distance_game_mp4/horray.mp3'
}

import pygame
pygame.mixer.init()
player = pygame.mixer.music

def game_setup():
    dst.setup_pins()
    player.load(COMMANDS.get('game_begin'))
    player.play()
    # player.set_volume(2.5)
    while player.get_busy():
        time.sleep(0.3)


def game(target = 100, thr=12):

    print("Starting game! Target={} (+/-{})".format(target, thr))
    found = False

    while not found:
        dist = dst.distance()

        if dist > target+thr:
            print('get closer', round(dist,2))
            player.load(COMMANDS.get('get_closer'))
            player.play()
        elif dist < target-thr:
            print('get far', round(dist,2))
            player.load(COMMANDS.get('get_far'))
            player.play()

        else:
            print('you found it!!!', dist, )
            player.load(COMMANDS.get('found'))
            player.play()
            found = True
            time.sleep(1)

        time.sleep(1.5)

    # Exit the player and clean all pins
    print ("Exiting game")#, player can quit:", player.can_quit())
    player.quit()

    import RPi.GPIO as GPIO
    GPIO.cleanup()
    print("Finished cleanup")


if __name__ == '__main__':
    game_setup()
    import random
    target = random.randint(80,160)
    game(target=target)
    print("Game Ended")



