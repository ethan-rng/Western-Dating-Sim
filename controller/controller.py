import pygame
import sys
import os

from controller.constants import *
from view.screens.chapters import *
from controller.GameSession import GameSession

# Importing Screens
from view.screens.menu import Menu
from view.screens.chapters.chapter1 import Chapter1
from view.screens.chapters.chapter2 import Chapter2
from view.screens.chapters.chapter3 import Chapter3
from view.screens.chapters.chapter4 import Chapter4
from view.screens.chapters.chapter5 import Chapter5
from view.screens.chapters.chapter6 import Chapter6


class runGame:
    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Dating Simulator Ver. Western")

        # Initializing Variables for PyGame
        self.GameSession = GameSession()
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

        # Controller Variables For The Game
        self.menu_state = "main"


        # Main Loop
        while True:
            if self.menu_state == "main":
                self.main_menu()
            elif self.menu_state == "settings":
                self.settings_main()
            elif self.menu_state == "chp1":
                Chapter1(self.screen, self.GameSession.player)
            elif self.menu_state == "chp2":
                Chapter2(self.screen, self.GameSession.player)
            elif self.menu_state == "chp3":
                Chapter3(self.screen, self.GameSession.player)
            elif self.menu_state == "chp4":
                Chapter4(self.screen, self.GameSession.player)
            elif self.menu_state == "chp5":
                Chapter5(self.screen, self.GameSession.player)
            elif self.menu_state == "chp6":
                Chapter6(self.screen, self.GameSession.player)
            else:
                pygame.quit()
                sys.exit()

    def main_menu(self):
        menu()

    def chapter1(self):
        chapter1_scene()

    def chapter2(self):
        pass

    def chapter3(self):
        pass

    def chapter4(self):
        pass

    def chapter5(self):
        pass

    def chapter6(self):
        pass
