"""
Module: test_player
Author: Jasper Yang
This module provides unit tests for the Player class.

"""

from models.Player import Player
from models.User import User
from models.exceptions import IllegalStats, UserNotFound
import os
import json
import unittest

class TestPlayer(unittest.TestCase):
    """
    Unit tests for the Player class.
    """

    def test_create_player(self):
        """
        Tests create player function.
        """
        # Create a player with too high stats
        lecia = Player()
        self.assertRaises(IllegalStats, lecia.create_player, "Lecia", "abcd", 20, 20, 20)
        # Create player
        lecia.create_player("Lecia", "abcd", 2, 2, 2)
        self.assertEqual(lecia.charisma, 2)
        self.assertEqual(lecia.attraction, 2)
        self.assertEqual(lecia.intelligence, 2)
        # Deletes Lecia from passwords
        for user in User.Users:
            if user["username"] == "Lecia":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

    def test_load_and_save_player(self):
        """
        Tests load and save player functions.
        """
        # Create a player
        aaron = Player()
        aaron.create_player("Aaron", "abcd", 2, 2, 2)
        # Saves Aaron's progress
        aaron.save_progress()
        # Load progress
        aaron2 = Player()
        aaron2.load_player("Aaron")
        self.assertEqual(aaron2.level, 1)
        self.assertEqual(aaron2.charisma, 2)
        self.assertEqual(aaron2.intelligence, 2)
        self.assertEqual(aaron2.attraction, 2)
        # Deletes Aaron from passwords
        for user in User.Users:
            if user["username"] == "Aaron":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
        # Deletes Aaron from gamestates
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            game_states = json.load(file)
            updated_game_states = [data for data in game_states if data["username"] != "Aaron"]
            with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
                json.dump(updated_game_states, file, indent=4)

    def test_update_stats(self):
        """
        Tests update stats function.
        """
        # Create Player
        ethan = Player()
        ethan.create_player("Ethan", "abcd", 2, 2, 2)
        # Update stats
        self.assertEqual(ethan.update_stats("Serena", 10), 12)
        # Deletes Ethan from passwords
        for user in User.Users:
            if user["username"] == "Ethan":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
        
    def test_get_final_score(self):
        """
        Tests get final score function.
        """
        # Create Player
        jasper = Player()
        jasper.create_player("Jasper", "abcd", 2, 2, 2)
        jasper.update_stats("Serena", 10)
        self.assertEqual(jasper.get_final_score(), 12)
        # Deletes Jasper from passwords
        for user in User.Users:
            if user["username"] == "Jasper":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

if __name__ == '__main__':
    unittest.main()
