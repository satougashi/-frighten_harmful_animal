#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time
from pathlib import Path
import random

def play_music(music_file_path, play_time):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play(-1) # 繰り返し

    time.sleep(play_time)
    pygame.mixer.music.stop()

# random.seed(0)
p = Path("../sound/")

sounds = list(p.glob("*.mp3"))
print(sounds)
play_music(random.choice(sounds).as_posix(), 5)