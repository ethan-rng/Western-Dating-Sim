from models.User import User
from models.Player import Player
from typing import List
import json, os
from models.exceptions import UserNotFound


class Instructor(User):
    Players: List['Player'] = []

    def __init__(self, password: str) -> None:
        super().__init__()
        super().login("instructor", password)
        Instructor._loadPlayers()

    # PRIVATE CLASS METHODS
    def _loadPlayers() -> None:
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            jsonData = json.load(file)
            Instructor.Players = []
            for data in jsonData:
                new_player = Player()
                new_player.loadPlayer(data["username"])
                Instructor.Players.append(new_player)

    # PUBLIC METHODS
    """ Public Method which allows the instructor to view the stats of a specific user (throws UserNotFound, IncorrectPrivilege exception) """
    def viewStats(self, username: str) -> dict:
        Instructor._loadPlayers()

        for player in Instructor.Players:
            if player.username == username:
                return {
                    "charisma": player.charisma,
                    "intelligence": player.intelligence,
                    "attraction": player.attraction
                }

        raise UserNotFound(username)

    """ Public Method which allows the instructor to view the progress of a specific user (throws IncorrectPrivilege exception) """
    def viewProgress(self, username: str) -> dict:
        Instructor._loadPlayers()

        for player in Instructor.Players:
            if player.username == username:
                return {
                    "level": player.level,
                    "attractionScore": player.attractionScore,
                }
        raise UserNotFound(username)
