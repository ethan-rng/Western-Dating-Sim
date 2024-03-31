import pygame
import sys
import os

from controller.constants import *
from view.screens.chapters import *

from view.screens.menu import Menu

class runGame:
    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Dating Simulator Ver. Western")

        # Initializing Variables 
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

        # Controller Variables For The Game
        self.menu_state = "main"
        self.scene_titles = {
            
        }

        # Main Loop
        while True:
            if self.menu_state == "main":
                self.main_menu()
            elif self.menu_state == "chp1":
                self.chapter1()
            elif self.menu_state == "chp2":
                self.chapter2()
            elif self.menu_state == "chp3":
                self.chapter3()
            elif self.menu_state == "chp4":
                self.chapter4()
            elif self.menu_state == "chp5":
                self.chapter5()
            elif self.menu_state == "chp6":
                self.chapter6()
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

    @staticmethod
    def updateScene(sceneIndex:int):
        pygame.display.set_caption(scene_titles[current_scene_index])  
        scene_title = SceneTitle(screen, scene_titles[current_scene_index] )
        scene_title.draw()
        pygame.display.flip()