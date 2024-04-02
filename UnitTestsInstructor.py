from models.User import User
from models.Player import Player
from models.Instructor import Instructor
from typing import List
import json, os
from models.exceptions import UserNotFound
import unittest

class testInstructor(unittest.TestCase):
    
    '''tests view stats and view progress'''
    def test_viewStats_and_progress(self):
        #the player that the instructor will be viewing
        Jasmine: Player = Player()
        Jasmine.createPlayer("Jasmine", "abcd", 2, 2, 2)
        Jasmine.saveProgress()
        #login to the instructor account
        Teacher:Instructor = Instructor("abcd")
        #view stats
        self.assertEqual(Teacher.viewStats("Jasmine")["charisma"], 2)
        self.assertEqual(Teacher.viewStats("Jasmine")["intelligence"], 2)
        self.assertEqual(Teacher.viewStats("Jasmine")["attraction"], 2)
        #view Progress
        self.assertEqual(Teacher.viewProgress("Jasmine")["level"], 1)
        self.assertEqual(Teacher.viewProgress("Jasmine")["attractionScore"], Jasmine.attractionScore)
        #deletes Jasmine from passwords
        for user in User.Users:
            if user["username"] == "Jasmine":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
        #deletes Jasmine from gamestates
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            game_states = json.load(file)
            updated_game_states = [data for data in game_states if data["username"] != "Jasmine"]
            with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
                json.dump(updated_game_states, file, indent=4) 

if __name__ == '__main__':
    unittest.main()