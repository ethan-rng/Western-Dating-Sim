import pygame
import sys
import os

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (160, 32, 240)
GRAY = (192, 192, 192)
DARK_GRAY = (132, 135, 140)
GREEN = (0, 255, 0)
LIGHT_GRAY = (234, 234, 234)

# CONSTANTS FOR CHAPTERS
SCENE_TITLES = {
    1: "SCENE 1: Talbot College",
    2: "SCENE 2: The Library Encounter",
    3: "SCENE 3: The Mysterious Forest",
    4: "SCENE 4: The Hidden Cave",
    5: "SCENE 5: The Final Showdown",
}

# CONSTANTS FOR THE GUI
pygame.init()

# Font setup
font = pygame.font.SysFont(None, 45)
title_font = pygame.font.SysFont(None, 90)
baby_font = pygame.font.SysFont(None, 20)

# Get the current display resolution
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h

# Sound being play
click_sfx = pygame.mixer.Sound(os.path.join('view', 'assets', 'click.wav'))
