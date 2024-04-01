import pygame
import sys
import os

from controller.constants import *
from view.screens.chapters import *

from view.screens.menu import Menu
from view.screens.settings.settingsMain import SettingsMain
from view.screens.settings.settingsControls import SettingsControls
from view.screens.settings.settingsSound import SettingsSound
from view.screens.help.help1 import Help1
from view.screens.help.help2 import Help2
from view.screens.newGame import NewGameScreen

class runGame:
    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Dating Simulator Ver. Western")

        # Initializing Variables 
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        self.menu = Menu()
        self.main_settings = SettingsMain()
        self.control_settings = SettingsControls()
        self.sound_settings = SettingsSound()
        self.help1_page = Help1()
        self.help2_page = Help2()
        self.new_game_screen = NewGameScreen()


        # Controller Variables For The Game
        self.menu_state = "main"
        self.scene_titles = {
            
        }

        # Main Loop
        while True:
            if self.menu_state == "main":
                self.main_menu()
            elif self.menu_state == "start":
                self.new_game()
            elif self.menu_state == "help1":
                self.help1()
            elif self.menu_state == "help2":
                self.help2()
            elif self.menu_state == "settings":
                self.settings_main()
            elif self.menu_state == "controls":
                self.settings_control()
            elif self.menu_state == "sound":
                self.settings_sound()
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
        self.menu_state = self.menu.event_handler(self.screen)
    
    def new_game(self):
        self.menu_state = self.new_game_screen.event_handler(self.screen)
    
    def help1(self):
        self.menu_state = self.help1_page.event_handler(self.screen)
        
    def help2(self):
        self.menu_state = self.help2_page.event_handler(self.screen)

    def settings_main(self):
        self.menu_state = self.main_settings.event_handler(self.screen)
        
    def settings_control(self):
        self.menu_state = self.control_settings.event_handler(self.screen)
    
    def settings_sound(self):
        self.menu_state = self.sound_settings.event_handler(self.screen)
    

        
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