import pygame
import sys
import os

from controller.constants import *
from view.screens.chapters import *
from controller.GameSession import GameSession

# Importing Screens
from view.screens.Menu import Menu
from view.screens.settings.SettingsMain import SettingsMain
from view.screens.settings.SettingsControls import SettingsControls
from view.screens.settings.SettingsSound import SettingsSound
from view.screens.help.Help1 import Help1
from view.screens.help.Help2 import Help2
from view.screens.NewGame import NewGameScreen
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
        self.menu = Menu()
        self.main_settings = SettingsMain()
        self.control_settings = SettingsControls()
        self.sound_settings = SettingsSound()
        self.help1_page = Help1()
        self.help2_page = Help2()
        self.new_game_screen = NewGameScreen()


        # Controller Variables For The Game
        self.menu_state = "main"
        self.controls = {} # issue

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
                SettingsMain(self.screen)
            elif self.menu_state == "controls":
                self.settings_control()
            elif self.menu_state == "sound":
                self.settings_sound()
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