#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time
import datetime
from pathlib import Path
import random
import os
import RPi.GPIO as GPIO

def play_music(music_file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    #print(music_file_path) 
    time.sleep(1)
    pygame.mixer.music.play() # no repeat

    time.sleep(1)
    while pygame.mixer.music.get_busy():
        time.sleep(1)

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

play_music(get_sound_path())
counter = 0
try:
    while True:
        if (GPIO.input(sensor_pin) == GPIO.HIGH):
            print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " sensor high")
            play_music(get_sound_path())
            time.sleep(sleeptime)
        else:
            time.sleep(1)
            counter = counter + 1
        
        if (counter > (60 * 15)):
            t = datetime.datetime.now().strftime("%H:%M")
            if (("00:00" <= t and t <= "05:00") or ("19:00" <= t and t <= "24:00")):
                print(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " timeout")
                for i in range(3):
                    play_music(get_sound_path())
                counter = 0
except KeyboardInterrupt:
    print("Quit")
finally:
    print("clean up")
    GPIO.cleanup()

