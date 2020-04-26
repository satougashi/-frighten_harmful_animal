#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time
from pathlib import Path
import random
import os

def play_music(music_file_path, play_time):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play(-1) # repeat

    time.sleep(play_time)
    pygame.mixer.music.stop()

# random.seed(0)
app_path = Path(os.path.abspath(os.getcwd())).parent
sount_path = Path(str(app_path) + "/sound/")
sounds = list(sount_path.glob("*.mp3"))

play_music(random.choice(sounds).as_posix(), 5)