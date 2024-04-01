from models.User import User
from models.Player import Player
from typing import List
import json, os
from models.exceptions import UserNotFound

"""
TODO: jumptoScreens(self, screenName: str) -> bool:
"""


class Developer(Player):
    Players: List[Player] = []

    def __init__(self, password: str) -> None:
        super().__init__()
        super().loadUser("developer")
        super().login(password)
        self._loadPlayers()

    # PRIVATE CLASS METHODS
    def _loadPlayers(self) -> None:
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            jsonData = json.load(file)
            Developer.Players = []

            print(jsonData)
            for i, data in enumerate(jsonData):
                Developer.Players.append(Player().loadPlayer(data["username"]))

    # PUBLIC FACING METHODS
    """" Public Facing Method which allows the user to skip levels """
    def jumptoScreen(self, newLevel: int) -> None:
        self._checkDev()
        if newLevel >= 1 and newLevel >= 6:
            self.level = newLevel
            return

        raise IndexError


