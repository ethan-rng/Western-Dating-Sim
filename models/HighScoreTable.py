import os, json
from models.exceptions import UserNotFound


class HighScoreTable:
    def __init__(self) -> None:
        self.scores: dict = self.getScores()

    # PUBLIC FACING METHODS
    """ Public Method which opens the json file and returns the scores dict """

    def getScores(self) -> dict:
        scores = {}
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            scores_list = json.load(file)
            for score in scores_list:
                scores[score["username"]] = score["finalScore"]
            return scores

    """ Public Method which allows the instructor to view the progress of a specific user (throws UserNotFound exception) """

    def getUserScore(self, username: str) -> int:
        self.getScores()

        for key in self.scores.keys():
            if key == username:
                return self.scores[key]
        raise UserNotFound(f"No user found with username {username}")

    """ Public Method which allows the instructor to view the progress of a specific user (throws IndexError exception) """
    
    def getRankScore(self, rank: int) -> tuple:
        sorted_scores = sorted(self.scores.items(), key = lambda x: x[1],reverse=True)
        return sorted_scores[rank-1]


