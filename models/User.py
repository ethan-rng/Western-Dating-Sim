from exceptions import UserAlreadyExists, UserNotFound, IncorrectPassword, AdminLevelAccount, IncorrectPrivilege
from typing import List
from hashlib import sha256
import os, json

class User:
    LoggedInUser:'User' = None
    Users:List[dict] = []

    def __init__(self) -> None:
        # Loading Users From Memory (only gets run on the first instance the class is called)
        if User.Users == []:
            with open(os.path.join("models", "data", "UserPasswords.json"), "r") as file:
                jsonData = json.load(file)

                for data in jsonData:
                    User.Users.append({
                        "username": data["username"], 
                        "password": data["password"],
                    })

        self.username = ""
        self._password = ""
    
    # PRIVATE METHODS
    """ Private method which checks if a user exists (throws UserNotFound exception) """
    def _userExists(self, username: str) -> bool:
        for user in User.Users:
            if user["username"] == username:
                return True
        return False
    
    # PROTECTED FACING METHODS
    """ Protected helper function which checks if the developer is logged in before allowing access (throws IncorrectPrivilege exception) """
    def _checkDev(self) -> None:
        if super().LoggedInUser != "developer":
            raise IncorrectPrivilege
    
    """ Protected helper function which checks if the instructor is logged in before allowing access (throws IncorrectPrivilege exception) """
    def _checkInstructor(self) -> None:
        if super().LoggedInUser != "instructor" and super().LoggedInUser!= "developer":
            raise IncorrectPrivilege
        
    """ Protected helper function which checks if the player is logged in before allowing access (throws IncorrectPrivilege exception) """
    def _checkPlayer(self) -> None:
        if super().LoggedInUser != self.username and super().LoggedInUser != "instructor" and super().LoggedInUser!= "developer":
            raise IncorrectPrivilege
        
    # PUBLIC METHODS
    """ Public facing method which makes a new player account (throws AdminLevelAccount and UserAlreadyExists exceptions) """
    def createUser(self, username, password) -> None:
        # Handling Dev and Instructor Account Creation
        if username == "developer" or username == "instructor":
            raise AdminLevelAccount
        
        # Handling Duplicate Account Creation
        if self._userExists(username):
            raise UserAlreadyExists(username)
            
        # Updating Instance Variable Values
        self.username = username
        self._password = sha256(password.encode()).hexdigest()

        # Updating Users List
        User.Users.append({"username": self.username, "password": self.password})

        # Updating users.json
        with open(os.path.join("models", "data", "UserPasswords.json"), 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.update({"username": self.username, "password": self._password})

    """ Public facing method which loads an existing user and their password to log into (throws UserNotFound exception)"""
    def loadUser(self, username: str) -> None:
        for user in User.Users:
            if user["username"] == username:
                self.username = username
                self._password = user["password"]
                return
        raise UserNotFound(username)

    """ Public facing method which logs in a user (throws IncorrectPassword exceptions) """
    def login(self, password: str) -> bool:
        if self._password == sha256(password.encode()).hexdigest() and (self._userExists(self.username) or self.username == "developer" or self.username == "instructor"):
            User.LoggedInUser = self
        raise IncorrectPassword(self.username, password)

    """ Public facing method which logs out a user """
    def logout(self) -> None:
        User.LoggedInUser = None
        self.username = ""
        self._password = ""
 
 