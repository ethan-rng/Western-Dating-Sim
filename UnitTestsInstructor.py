"""
Module: test_instructor
Author: Jasper Yang
This module provides unit tests for the Instructor class.

"""

from models.User import User
from models.Player import Player
from models.Instructor import Instructor
from typing import List
import json
import os
from models.exceptions import UserNotFound
import unittest

class TestInstructor(unittest.TestCase):
    """
    Unit tests for the Instructor class.
    """

    def test_view_stats_and_progress(self):
        """
        Tests view stats and view progress functions.
        """
        # The player that the instructor will be viewing
        jasmine = Player()
        jasmine.createPlayer("Jasmine", "abcd", 2, 2, 2)
        jasmine.saveProgress()
        # Login to the instructor account
        teacher = Instructor("abcd")
        # View stats
        self.assertEqual(teacher.viewStats("Jasmine")["charisma"], 2)
        self.assertEqual(teacher.viewStats("Jasmine")["intelligence"], 2)
        self.assertEqual(teacher.viewStats("Jasmine")["attraction"], 2)
        # View progress
        self.assertEqual(teacher.viewProgress("Jasmine")["level"], 1)
        self.assertEqual(teacher.viewProgress("Jasmine")["attractionScore"], jasmine.attractionScore)
        # Deletes Jasmine from passwords
        for user in User.Users:
            if user["username"] == "Jasmine":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
        # Deletes Jasmine from gamestates
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            game_states = json.load(file)
            updated_game_states = [data for data in game_states if data["username"] != "Jasmine"]
            with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
                json.dump(updated_game_states, file, indent=4) 

if __name__ == '__main__':
    unittest.main()

