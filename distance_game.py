#!/usr/bin/python3

from breadboard import distance_meassure as d
import time

COMMANDS = {
    'get_closer': '/home/pi/Music/distance_commands/get_closer.m4a',
    'get_far': '/home/pi/Music/distance_commands/get_far.m4a',
    'game_begin': '/home/pi/Music/distance_commands/game_begin.m4a',
    'found': '/home/pi/Music/distance_commands/horray.m4a'
}

from omxplayer.player import OMXPlayer
player = None

def game_setup():
    player = OMXPlayer(COMMANDS.get('game_begin'), args=['-o', 'alsa'])
    player.set_volume(2.5)
    time.sleep(1)
    # player = OMXPlayer('/home/pi/Music/distance_commands/get_closer.m4a', args=['-o', 'alsa'], pause=True)


def game(target = 100, thr=12):

    print("Starting game! Target={} (+/-{})".format(target, thr))
    found = False

    while not found:
        dist = d.distance()

        if dist > target+thr:
            print('get closer', round(dist,2))
            player = OMXPlayer(COMMANDS.get('get_closer'), args=['-o', 'alsa'])
        elif dist < target-thr:
            print('get far', round(dist,2))
            player = OMXPlayer(COMMANDS.get('get_far'), args=['-o', 'alsa'])
        else:
            print('you found it!!!', dist, )
            player = OMXPlayer(COMMANDS.get('found'), args=['-o', 'alsa'])
            found = True
            time.sleep(1)

        time.sleep(1.5)

    print ("Exiting game")#, player can quit:", player.can_quit())
    player.quit()


if __name__ == '__main__':
    game_setup()
    import random
    target = random.randint(80,160)
    game(target=target)
    print("Game Ended")
    import RPi.GPIO as GPIO
    GPIO.cleanup()
    print("Finished cleanup")



