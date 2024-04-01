from models.User import User
from models.Player import Player
from typing import List
import json, os
from models.exceptions import UserNotFound

"""
TODO: jumptoScreens(self, screenName: str) -> bool:
TODO: debug(self, screenName: str) -> bool:

"""


class Developer(Player):
    Players: List[Player] = []

    def __init__(self, password: str) -> None:
        super().__init__()
        super().login("developer", password)
        Developer._loadPlayers()

    # PRIVATE CLASS METHODS
    def _loadPlayers(self) -> None:
        with open(os.path.join('models', 'data', 'Developers.json'), "r") as file:
            jsonData = json.load(file)
            Developer.Players = []

            for data in jsonData:
                Developer.Players.append(Player().loadPlayer(data["username"]))

    # PUBLIC FACING METHODS
    """ Public Method which allows the change any user's stats (throws IncorrectPrivilege, KeyError and UserNotFound exception) """

    def modifyUserStats(self, username: str, character: str, stat: int, attrib: str = ""):
        self._checkDev()

        # Handling Non Existing Username
        for player in Developer.Players:
            if player.username == username:
                if character == "self":
                    if attrib == "charisma":
                        player.charisma = stat
                    elif attrib == "intel":
                        player.intelligence = stat
                    elif attrib == "attraction":
                        player.attraction = stat
                    elif attrib == "level":
                        player.level = stat
                    else:
                        raise KeyError(attrib)
                else:
                    # Will raise KeyError if character does not exist
                    player.attractionScore[character] = stat

                player.saveProgress()

        raise UserNotFound(username)

    """ Public Method which returns a dictionary of various debugging data (throws IncorrectPrivilege exception) """

    # ! WORKING IN PROGRESS
    def debugGame(self) -> dict:
        self._checkDev()

    """ Public Method which allows the developer to jump to a specific screen (throws IncorrectPrivilege exception) """

    # ! WORKING IN PROGRESS
    def jumptoScreen(self, screen: str) -> None:
        self._checkDev()
