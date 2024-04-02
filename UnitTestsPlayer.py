from models.Player import Player
from models.User import User
from models.exceptions import IllegalStats, UserNotFound
import os, json
import unittest

#unit tests for Player class
class testPlayer(unittest.TestCase):

    '''tests create player'''
    def test_createPlayer(self):
        #create a player with too high stats
        Lecia: Player = Player()
        self.assertRaises(IllegalStats, Lecia.createPlayer, "Lecia", "abcd", 20, 20, 20)
        #create player
        Lecia.createPlayer("Lecia", "abcd", 2, 2, 2)
        self.assertEqual(Lecia.charisma, 2)
        self.assertEqual(Lecia.attraction, 2)
        self.assertEqual(Lecia.intelligence, 2)
        #deletes Lecia from passwords
        for user in User.Users:
            if user["username"] == "Lecia":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

    '''tests load and save player'''
    def test_load_and_save_Player(self):
        #create a player
        Aaron:Player = Player()
        Aaron.createPlayer("Aaron", "abcd", 2, 2, 2)
        #saves Aaron's progress
        Aaron.saveProgress()
        #load progress
        Aaron2: Player = Player()
        Aaron2.loadPlayer("Aaron")
        self.assertEqual(Aaron2.level, 1)
        self.assertEqual(Aaron2.charisma, 2)
        self.assertEqual(Aaron2.intelligence, 2)
        self.assertEqual(Aaron2.attraction, 2)
        #deletes Aaron from passwords
        for user in User.Users:
            if user["username"] == "Aaron":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
        #deletes Aaron from gamestates
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            game_states = json.load(file)
            updated_game_states = [data for data in game_states if data["username"] != "Aaron"]
            with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
                json.dump(updated_game_states, file, indent=4)

    '''tests update stats'''
    def test_updateStats(self):
        #create Player
        Ethan:Player = Player()
        Ethan.createPlayer("Ethan", "abcd", 2, 2, 2)
        #update stats
        self.assertEqual(Ethan.updateStats("Serena", 10), 12)
        #deletes Ethan from passwords
        for user in User.Users:
            if user["username"] == "Ethan":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
        
    def test_getFinalScore(self):
        #create Player
        Jasper:Player = Player()
        Jasper.createPlayer("Jasper", "abcd", 2, 2, 2)
        Jasper.updateStats("Serena", 10)
        self.assertEqual(Jasper.getFinalScore(), 12)
        #deletes Jasper from passwords
        for user in User.Users:
            if user["username"] == "Jasper":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

if __name__ == '__main__':
    unittest.main()