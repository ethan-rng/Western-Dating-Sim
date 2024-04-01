import pygame
import sys
import os

from controller.constants import *
from view.screens.chapters import *
from controller.GameSession import GameSession

# Importing Screens
from view.screens.Menu import Menu
from view.screens.settings.SettingsMain import SettingsMain
from view.screens.chapters.Chapter1 import Chapter1
from view.screens.chapters.Chapter2 import Chapter2
from view.screens.chapters.Chapter3 import Chapter3
from view.screens.chapters.Chapter4 import Chapter4
from view.screens.chapters.Chapter5 import Chapter5
from view.screens.chapters.Chapter6 import Chapter6


class RunGame:
    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Dating Simulator Ver. Western")

        # Initializing Variables for PyGame
        self.GameSession = GameSession()
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

        # Controller Variables For The Game
        self.menu_state = "main"
        self.controls = {} # issue

        # Main Loop
        while True:
            if self.menu_state == "main":
                Menu(self.screen)
            elif self.menu_state == "settings":
                SettingsMain(self.screen)
            elif self.menu_state == "chp1":
                Chapter1(self.screen,
                         self.GameSession.player,
                         "Chapter 1",
                         [
                             "A bustling Talbot College hallway...",
                             "You bump into a hurried girl (LI), causing her to drop her music score...",
                             "Oh, sorry! Gotta run!!",
                             "Y/N : Wait!",
                             "She runs off, and you notice a music sheet with contact info for an exam..",
                             "Narrator: She's gone but left a dropped sheet with her contact. Do you return it?"
                         ],
                         [
                             os.path.join('view', 'assets', 'chp1', 'talbot-1.jpg'),
                             os.path.join('view', 'assets', 'chp1', 'talbot-2.jpg'),
                             os.path.join('view', 'assets', 'chp1', 'talbot-3.jpg'),
                             os.path.join('view', 'assets', 'chp1', 'talbot-4.jpg'),
                             os.path.join('view', 'assets', 'chp1', 'talbot-5.jpg'),
                             os.path.join('view', 'assets', 'chp1', 'talbot-6.jpg')
                         ],
                         self.controls
                         )

            elif self.menu_state == "chp2":
                pass
                # Chapter2(self.screen, self.GameSession.player)
            elif self.menu_state == "chp3":
                pass
                # Chapter3(self.screen, self.GameSession.player)
            elif self.menu_state == "chp4":
                pass
                # Chapter4(self.screen, self.GameSession.player)
            elif self.menu_state == "chp5":
                pass
                # Chapter5(self.screen, self.GameSession.player)
            elif self.menu_state == "chp6":
                pass
                # Chapter6(self.screen, self.GameSession.player)
            else:
                pygame.quit()
                sys.exit()


