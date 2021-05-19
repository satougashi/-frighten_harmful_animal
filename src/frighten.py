#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time
import datetime
from pathlib import Path
import random
import os
import RPi.GPIO as GPIO

speaker_pin = 17

# random.seed(0)
def get_sound_path():
    app_path = Path(os.path.abspath(__file__)).parents[1]
    sount_path = Path(str(app_path) + "/sound/")
    sounds = list(sount_path.glob("*.mp3"))
    return random.choice(sounds).as_posix()

def play_music():
    GPIO.output(speaker_pin, 1)
    pygame.mixer.init()

    play_second = 0
    while play_second < 60:
        music_file_path = get_sound_path()
        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.play() # no repeat

        while pygame.mixer.music.get_busy():
            play_second = play_second + 1
            time.sleep(1)

# sensor_pin = 18
sleeptime = 1
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
# GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(speaker_pin, GPIO.OUT)

play_music()
counter = 0
try:
    while True:
        GPIO.output(speaker_pin, 0)
        # if (GPIO.input(sensor_pin) == GPIO.HIGH):
        #     print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " sensor high")
        #     play_music(get_sound_path())
        #     time.sleep(sleeptime)
        # else:
        time.sleep(1)
        counter = counter + 1
        
        if (counter > (60 * 30)):
            t = datetime.datetime.now().strftime("%H:%M")
            if (("00:00" <= t and t <= "06:00") or ("19:00" <= t and t <= "24:59")):
                print(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " timeout")
                play_music()
                counter = 0
except KeyboardInterrupt:
    print("Quit")
finally:
    print("clean up")
    GPIO.cleanup()

