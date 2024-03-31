from models.User import User
from models.Player import Player
from models.Developer import Developer
from models.Instructor import Instructor
from models.HighScoreTable import HighScoreTable

from typing import List
import os, json


class GameSession:
    def __init__(self):
        self.currPlayer: User = None
        self.currentLevel: int = None
        self.highScoreTable: HighScoreTable = HighScoreTable()


    # Sets Game To Appropriate Level
    def startNewGame(self, username:str, ) -> bool:
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

    def quitGame(self):
        pass

