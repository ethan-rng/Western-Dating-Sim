"""
Module: highscore_table_model
Author Ethan Rong, Aaron XIe, Jasper Yang
This module provides the HighScoreTable class for managing high scores.

"""

import os
import json
from models.exceptions import UserNotFound


class HighScoreTable:
    """
    A class to represent a high score table.

    Attributes:
    - scores: a dictionary containing the high scores

    Methods:
    - __init__: initializes the HighScoreTable instance
    - getScores: public method to retrieve the high scores from disk
    - getUserScore: public method to retrieve the score of a specific user
    - getRankScore: public method to retrieve the score at a specific rank
    """

    def __init__(self) -> None:
        """
        Initializes the HighScoreTable instance.
        """
        self.scores: dict = self.getScores()

    def getScores(self) -> dict:
        """
        Public method to retrieve the high scores from disk.

        Returns:
        - dict: a dictionary containing the high scores
        """
        scores = {}
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            scores_list = json.load(file)
            for score in scores_list:
                scores[score["username"]] = score["finalScore"]
            return scores

    def getUserScore(self, username: str) -> int:
        """
        Public method to retrieve the score of a specific user.

        Parameters:
        - username: the username of the user whose score is to be retrieved

        Returns:
        - int: the score of the specified user

        Raises:
        - UserNotFound: if the specified user does not exist
        """
        self.getScores()

        for key in self.scores.keys():
            if key == username:
                return self.scores[key]
        raise UserNotFound(f"No user found with username {username}")

    def getRankScore(self, rank: int) -> tuple:
        """
        Public method to retrieve the score at a specific rank.

        Parameters:
        - rank: the rank of the score to be retrieved

        Returns:
        - tuple: a tuple containing the username and score at the specified rank

        Raises:
        - IndexError: if the rank is out of bounds
        """
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[rank - 1]


