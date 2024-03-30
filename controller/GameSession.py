from models import *

from Users.User import User
from Users.Player import Player
from Users.Developer import Developer
from Users.Instructor import Instructor

from models.HighScoreTable import HighScoreTable
from models.MusicPlayer import MusicPlayer
from models.NPC import NPC

from typing import List
import json


class GameSession:
    def __init__(self):
        # Component Level Instance Variables
        self.musicPlayer: MusicPlayer = MusicPlayer()
        self.highScoreTable: HighScoreTable = HighScoreTable()
        self._npcs: List[NPC] = [
            NPC("Serena", ["charisma", "intel"]),
            NPC("Grace", ["attraction"]),
            NPC("Afnan", ["intel", "attraction"]),
            NPC("Jack", ["charisma"])
        ]

        # User Level Instance Variables
        self.currentUser = None
        self.currentLevel: int = 0
    

        # No fucking clue what this does
        self._playerState: bool = None 

    # USER LEVEL METHODS
    def setUser(self, username) -> bool:
        if username == "developer":
        elif username == "instructor":
            self.user
        else:



    # GAME LEVEL METHODS
    # Sets Game To Appropriate Level
    def startNewGame(self, username: str, password: int) -> bool:
        # Creates New User

        pass

    # Loads Game Based On Individual User
    def loadGame(self, username: str, password: str) -> bool:
        # Attempts to Log In User

        # Sets Game Up With Right Dialogue Based On User's Stats
        pass

    # Saves Game
    def saveGame(self):
        # Saves Player Progression to File
        User.saveAllUsers()

        pass


