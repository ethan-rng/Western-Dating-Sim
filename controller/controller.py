import pygame
import sys
import os

from controller.constants import *
from view.screens.chapters import *
from models.Player import Player

# Importing Screens
from view.screens.Menu import Menu
from view.screens.NewGame import NewGameScreen
from view.screens.settings.SettingsMain import SettingsMain
from view.screens.settings.SettingsControls import SettingsControls
from view.screens.settings.SettingsSound import SettingsSound
from view.screens.help.Help1 import Help1
from view.screens.help.Help2 import Help2
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
        self.currPlayer: Player = Player()
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

        # Controller Variables For The Game
        self.game_state = "main"
        self.controls = {}  # issue

        # Main Loop (Determines Which Screen To Display)
        while True:
            if self.game_state == "main":
                self.game_state = Menu().event_handler(self.screen)
            elif self.game_state == "start":
                self.game_state = NewGameScreen().event_handler(self.screen)
            elif self.game_state == "help1":
                self.game_state = Help1().event_handler(self.screen)
            elif self.game_state == "help2":
                self.game_state = Help2().event_handler(self.screen)
            elif self.game_state == "settings":
                self.game_state = SettingsMain().event_handler(self.screen)
            elif self.game_state == "controls":
                self.game_state = SettingsControls().event_handler(self.screen)
            elif self.game_state == "sound":
                SettingsSound().event_handler(self.screen)
            elif self.game_state == "chp" and self.currPlayer.level == 1:
                self.game_state = Chapter1(self.screen,
                                           self.currPlayer,
                                           "Chapter 1",
                                           [
                                               "A bustling Talbot College hallway...",
                                               f"You bump into a hurried girl, causing her to drop her music score...",
                                               "Oh, sorry! Gotta run!!",
                                               f"{self.currPlayer.username} : Wait!",
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
                                           ).event_handler()

            elif self.game_state == "chp" and self.currPlayer.level == 2:
                self.game_state = Chapter2(self.screen,
                                           self.currPlayer,
                                           "Chapter 2",
                                           [
                                               "You agree to meet up at UCC to return the sheet music.",
                                               "She thanks you, and you guys decide to grab something to eat at the Spoke..",
                                               "What do you talk about in line?",
                                               "How do you respond?"
                                           ],
                                           [
                                               os.path.join('view', 'assets', 'chp2', 'spoke-1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-4.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-4.1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-4.2.jpg'),
                                           ],
                                           self.controls
                                           ).event_handler()
            elif self.game_state == "chp" and self.currPlayer.level == 3:
                pass
                # Chapter3(self.screen, self.GameSession.player)
            elif self.game_state == "chp" and self.currPlayer.level == 4:
                pass
                # Chapter4(self.screen, self.GameSession.player)
            elif self.game_state == "chp" and self.currPlayer.level == 5:
                pass
                # Chapter5(self.screen, self.GameSession.player)
            elif self.game_state == "chp" and self.currPlayer.level == 6:
                pass
                # Chapter6(self.screen, self.GameSession.player)
            else:
                print(self.game_state)
                print(self.currPlayer.level)
                pygame.quit()
                sys.exit()
