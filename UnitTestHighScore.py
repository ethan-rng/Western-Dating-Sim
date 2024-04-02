import os, json
from models.HighScoreTable import HighScoreTable
from models.exceptions import UserNotFound
from models.Player import Player
from models.User import User
import unittest

class testHighScore(unittest.TestCase):
    
    '''test get scores'''

    def test_getScores(self):
        #create the highscores table
        Hscores: HighScoreTable = HighScoreTable()
        #create a player to put on the highscores table
        Aaron: Player = Player()
        Aaron.createPlayer("Aaron", "abcd", 0, 0, 0)
        #give the player some score
        Aaron.updateStats("Serena", 10)
        #saves the score
        Aaron.saveProgress()
        #gets the scores
        self.assertEqual(Hscores.getScores()["Aaron"], 10)
        #deletes Aaron and Jasper from passwords
        for user in User.Users:
            if user["username"] == "Aaron":
                User.Users.remove(user)
                break;
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

        #deletes Aaron from gamestates
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            game_states = json.load(file)
            updated_game_states = [data for data in game_states if data["username"] != "Aaron"]
            with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
                json.dump(updated_game_states, file, indent=4)
    
    def test_RankScore(self):
        #create the highscores table
        Hscores: HighScoreTable = HighScoreTable()
        #gets the ranks
        self.assertEqual(Hscores.getRankScore(1), ('ggg', 0))
if __name__ == '__main__':
    unittest.main()