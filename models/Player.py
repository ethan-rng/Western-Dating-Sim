"""
Module: player_model
Author: Jasper Yang, Ethan Rong, Aaron Xie
This module provides the Player class for managing player accounts and game states.

"""

from models.User import User
from models.exceptions import IllegalStats, UserNotFound
from typing import List
import os
import json

# CONSTANTS
MAX_SCORE = 10
CHARACTER_BIAS = {
    "Serena": ["charisma", "intel"]
}


class Player(User):
    """
    A class to represent player accounts and game states.

    Attributes:
    - Players: class variable representing a list of player data

    Methods:
    - __init__: initializes the Player instance
    - createPlayer: public method to create a new player account
    - loadPlayer: public method to load an existing player account
    - saveProgress: public method to save player progress
    - updateStats: public method to update player stats after an interaction
    - getFinalScore: public method to calculate the final score of the player
    """

    Players: List[dict] = []

    def __init__(self) -> None:
        """
        Initializes the Player instance.
        Loads player data from memory (only runs on the first instance the class is called).
        """
        super().__init__()
        if not Player.Players:
            with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
                jsonData = json.load(file)
                for data in jsonData:
                    Player.Players.append({
                        "username": data["username"],
                        "level": data["level"],
                        "charisma": data["charisma"],
                        'intel': data["intel"],
                        "attraction": data["attraction"],
                        "attractionScore": data["attractionScore"],
                        "finalScore": data["finalScore"],
                    })

        # Base Stats
        self._level = 1
        self._charisma = 0
        self._intelligence = 0
        self._attraction = 0

        # Individual Attraction Score
        self._attractionScore = {
            "Serena": 0,
        }

    def createPlayer(self, username: str, password: str, charisma: int, intel: int, attraction: int) -> None:
        """
        Public method to create a new player account.

        Parameters:
        - username: the username of the new player
        - password: the password of the new player
        - charisma: the charisma stat of the new player
        - intel: the intelligence stat of the new player
        - attraction: the attraction stat of the new player

        Raises:
        - IllegalStats: if the sum of charisma, intelligence, and attraction is greater than MAX_SCORE
        """
        if charisma + intel + attraction > MAX_SCORE or (charisma < 0 or intel < 0 or attraction < 0):
            raise IllegalStats(charisma, intel, attraction)

        super().createUser(username, password)

        # Base Stats
        self._level = 1
        self._charisma = charisma
        self._intelligence = intel
        self._attraction = attraction

        # Individual Attraction Score
        self._attractionScore = {
            "Serena": 0,
        }

    def loadPlayer(self, username: str) -> None:
        """
        Public method to load an existing player account.

        Parameters:
        - username: the username of the player to load

        Raises:
        - UserNotFound: if the player does not exist
        """
        super().loadUser(username)
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            jsonData = json.load(file)
            for data in jsonData:
                if data["username"] == username:
                    self._level = data["level"]
                    self._charisma = data["charisma"]
                    self._intelligence = data["intel"]
                    self._attraction = data["attraction"]
                    self._attractionScore = data["attractionScore"]
                    return
                
            raise UserNotFound(username)

    def saveProgress(self) -> None:
        """
        Public method to save player progress.
        """
        with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
            playerData = {
                "username": self.username,
                "level": self._level,
                "charisma": self._charisma,
                "intel": self._intelligence,
                "attraction": self._attraction,
                "attractionScore": self._attractionScore,
                "finalScore": self.getFinalScore(),
            }
            Player.Players.append(playerData)
            json.dump(Player.Players, file, ensure_ascii=False, indent=4)

    def updateStats(self, character: str, newAttractionScore: int) -> int:
        """
        Public method to update player stats after an interaction.

        Parameters:
        - character: the character associated with the interaction
        - newAttractionScore: the new attraction score obtained from the interaction

        Returns:
        - int: the updated attraction score for the character
        """
        if self._attractionScore[character] >= 100 and newAttractionScore > 0:
            print(f"Attraction Score Maxed Out With {character}")
            return 100
        if self._attractionScore[character] <= 0 and newAttractionScore < 0:
            print(f"Attraction Score Minimized With {character}")
            return 0

        bias = 0
        for characterBias in CHARACTER_BIAS[character]:
            if characterBias == "charisma":
                bias += self._charisma
            elif characterBias == "intel":
                bias += self._intelligence
            elif characterBias == "attraction":
                bias += self._attraction

        self._attractionScore[character] += newAttractionScore * (bias * 0.1 * 0.5 + 1)
        return self._attractionScore[character]

    def getFinalScore(self) -> int:
        """
        Public method to calculate the final score of the player.

        Returns:
        - int: the final score of the player
        """
        finalScore = 0
        for score in self._attractionScore.values():
            finalScore += score

        return finalScore

    # SETTERS AND GETTERS
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, value):
        self._charisma = value

    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        self._intelligence = value

    @property
    def attraction(self):
        return self._attraction

    @attraction.setter
    def attraction(self, value):
        self._attraction = value

    @property
    def attractionScore(self):
        return self._attractionScore

    @attractionScore.setter
    def attractionScore(self, value):
        self._attractionScore = value
