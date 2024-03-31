from models.User import User
from models.Player import Player
from typing import List
import json, os

"""
TODO: viewStats(self, username: str) -> bool: {not sure how to do if Developers are not inheriting from Player}
TODO: viewProgress(self, username: str) -> bool: {not sure what view progress will look like}
"""

class Instructor(User):
    Players:List['Player'] = []
    PASSWORD:str = ""

    def __init__(self, password: str) -> bool:
        if Instructor.PASSWORD == "":
            with open("../AdminPasswords.json", "r") as file:
                jsonData = json.load(file)
                self.Password = jsonData["instructor"]

        if Instructor.Players == []:
            with open("../data/UserGameStat.json", "r") as file:
                jsonData = json.load(file)
                for data in jsonData:
                    Instructor.Players.append(Player(data["username"], data["password"], data["charisma"], data["intel"], data["attraction"]))

        return super().login("instructor", password)

    """ Public Method which allows the instructor to view the stats of a specific user (throws IncorrectPrivilege exception) """
    #! WORKING IN PROGRESS
    def viewStats(self, screen: str) -> bool:
        if super().LoggedInUser != "developer":
            return False
        

        return True
        
    """ Public Method which allows the instructor to view the progress of a specific user (throws IncorrectPrivilege exception) """
    #! WORKING IN PROGRESS
    def viewProgress(self, username) -> bool:
        if super().LoggedInUser != "developer":
            return False
        
        # Code Modify User Stats

        return True
