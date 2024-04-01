import os, json
from models.exceptions import UserNotFound


class HighScoreTable:
    def __init__(self) -> None:
        self.scores: dict = self.getScores()

    # PUBLIC FACING METHODS
    """ Public Method which opens the json file and returns the scores dict """

    def getScores(self) -> list:
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            self.scores = list(json.load(file))
            return self.scores

    """ Public Method which allows the instructor to view the progress of a specific user (throws UserNotFound exception) """

    def getUserScore(self, username: str) -> int:
        self.getScores()

        for player in self.scores:
            if player["username"] == username:
                return player["finalScore"]
        raise UserNotFound(f"No user found with username {username}")

    """ Public Method which allows the instructor to view the progress of a specific user (throws IndexError exception) """

    def getRankScore(self, rank: int) -> str:
        scores = list(self.scores.values())
        scores.sort(key=lambda x: x["finalScore"], reverse=True)

        return scores[rank - 1]
