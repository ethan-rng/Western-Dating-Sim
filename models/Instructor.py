"""
Module: instructor_model
Authors: Ethan Rong, Jasper Yang, Aaron Xie
This module provides the Instructor class for managing instructor accounts and interacting with player data.

"""

from models.User import User
from models.Player import Player
from typing import List
import json
import os
from models.exceptions import UserNotFound


class Instructor(User):
    """
    A class to represent instructor accounts and interact with player data.

    Attributes:
    - Players: class variable representing a list of player instances

    Methods:
    - __init__: initializes the Instructor instance and loads player data
    - _loadPlayers: private class method to load player data from disk
    - viewStats: public method to view the stats of a specific user
    - viewProgress: public method to view the progress of a specific user
    """

    Players: List['Player'] = []

    def __init__(self, password: str) -> None:
        """
        Initializes the Instructor instance and loads player data.
        
        Parameters:
        - password: the password of the instructor account
        """
        super().__init__()
        super().login("instructor", password)
        Instructor._loadPlayers()

    @staticmethod
    def _loadPlayers() -> None:
        """
        Private class method to load player data from disk.
        """
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            jsonData = json.load(file)
            Instructor.Players = []
            for data in jsonData:
                new_player = Player()
                new_player.loadPlayer(data["username"])
                Instructor.Players.append(new_player)

    def viewStats(self, username: str) -> dict:
        """
        Public method to view the stats of a specific user.

        Parameters:
        - username: the username of the user whose stats are to be viewed

        Returns:
        - dict: a dictionary containing the stats of the specified user

        Raises:
        - UserNotFound: if the specified user does not exist
        """
        Instructor._loadPlayers()

        for player in Instructor.Players:
            if player.username == username:
                return {
                    "charisma": player.charisma,
                    "intelligence": player.intelligence,
                    "attraction": player.attraction
                }

        raise UserNotFound(username)

    def viewProgress(self, username: str) -> dict:
        """
        Public method to view the progress of a specific user.

        Parameters:
        - username: the username of the user whose progress is to be viewed

        Returns:
        - dict: a dictionary containing the progress of the specified user

        Raises:
        - UserNotFound: if the specified user does not exist
        """
        Instructor._loadPlayers()

        for player in Instructor.Players:
            if player.username == username:
                return {
                    "level": player.level,
                    "attractionScore": player.attractionScore,
                }
        raise UserNotFound(username)
