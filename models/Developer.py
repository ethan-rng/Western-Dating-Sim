"""
Module: developer_model
Authors: Ethan Rong, Jasper Yang, Aaron Xie
This module provides the Developer class for managing developer functionalities.

"""

from models.User import User
from models.Player import Player
from typing import List
import json
import os
from models.exceptions import UserNotFound

class Developer(Player):
    """
    A class to represent a developer.

    Attributes:
    - Players: a list of Player instances

    Methods:
    - __init__: initializes the Developer instance
    - _loadPlayers: private method to load player instances from disk
    - jumptoScreen: public method to skip levels
    """

    Players: List[Player] = []

    def __init__(self, password: str) -> None:
        """
        Initializes the Developer instance.

        Parameters:
        - password: the password for the developer account
        """
        super().__init__()
        super().loadUser("developer")
        super().login("developer", password)
        self._loadPlayers()

    def _loadPlayers(self) -> None:
        """
        Private method to load player instances from disk.
        """
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            jsonData = json.load(file)
            Developer.Players = []

            for i, data in enumerate(jsonData):
                Developer.Players.append(Player().loadPlayer(data["username"]))

    def jumptoScreen(self, newLevel: int) -> None:
        """
        Public method to skip levels.

        Parameters:
        - newLevel: the level to jump to

        Raises:
        - IndexError: if the specified level is out of bounds
        """
        self._checkDev()
        if newLevel >= 1 and newLevel <= 6:
            self.level = newLevel
            return

        raise IndexError

