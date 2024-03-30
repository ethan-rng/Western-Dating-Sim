from models.User import User
from models.Player import Player
from typing import List
import json, os
from models.exceptions import UserNotFound

"""
TODO: jumptoScreens(self, screenName: str) -> bool:
TODO: debugGame(self) -> bool
"""

class Developer(Player):
    Players:List[Player] = []

    def __init__(self) -> None:
        # Loading Users From Memory (only gets run on the first instance the class is called)
        if len(Developer.Players) == 0:
            with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
                jsonData = json.load(file)
                for data in jsonData:
                    Developer.Players.append(Player().loadPlayer(data["username"]))
    
        super().__init__()
    

    # PUBLIC FACING METHODS
    """ Public Method which allows the developer to jump to a specific screen (throws IncorrectPrivilege exception) """
    # ! WORKING IN PROGRESS
    def jumptoScreen(self, screen:str) -> None:
        self._checkDev()


    """ Public Method which allows the change any user's stats (throws IncorrectPrivilege, KeyError and UserNotFound exception) """
    def modifyUserStats(self, username:str, character:str, stat:int, attrib:str=""):
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