#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time
from pathlib import Path
import random
import os
import RPi.GPIO as GPIO

def play_music(music_file_path, play_time):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play(-1) # repeat

    time.sleep(play_time)
    pygame.mixer.music.stop()

# random.seed(0)
def get_sound_path():
    app_path = Path(os.path.abspath(__file__)).parents[1]
    sount_path = Path(str(app_path) + "/sound/")
    sounds = list(sount_path.glob("*.mp3"))
    return random.choice(sounds).as_posix()

sensor_pin = 18
sleeptime = 1
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        if (GPIO.input(sensor_pin) == GPIO.HIGH):
            play_music(get_sound_path(), 5)
            time.sleep(sleeptime)
        else:
            time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
finally:
    print("clean up")
    GPIO.cleanup()

