"""
Module: test_high_score
Author: Jasper Yang
This module provides unit tests for the HighScoreTable class.

"""

import os
import json
from models.HighScoreTable import HighScoreTable
from models.exceptions import UserNotFound
from models.Player import Player
from models.User import User
import unittest

class TestHighScore(unittest.TestCase):
    """
    Unit tests for the HighScoreTable class.
    """

    def test_get_scores(self):
        """
        Tests get scores function.
        """
        # Create the highscores table
        hscores = HighScoreTable()
        # Create a player to put on the highscores table
        aaron = Player()
        aaron.createPlayer("Aaron", "abcd", 0, 0, 0)
        # Give the player some score
        aaron.updateStats("Serena", 10)
        # Save the score
        aaron.saveProgress()
        # Gets the scores
        self.assertEqual(hscores.getScores()["Aaron"], 10)
        # Deletes Aaron from passwords
        for user in User.Users:
            if user["username"] == "Aaron":
                User.Users.remove(user)
                break
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

        # Deletes Aaron from gamestates
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            game_states = json.load(file)
            updated_game_states = [data for data in game_states if data["username"] != "Aaron"]
            with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
                json.dump(updated_game_states, file, indent=4)
    
    def test_rank_score(self):
        """
        Tests rank score function.
        """
        # Create the highscores table
        hscores = HighScoreTable()
        # Gets the ranks
        self.assertEqual(hscores.getRankScore(1), ('joe', 15))

if __name__ == '__main__':
    unittest.main()

