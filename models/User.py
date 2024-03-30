import json
from exceptions import UserAlreadyExists, UserNotFound, IncorrectPassword, AdminLevelAccount
from typing import List
from hashlib import sha256

class User:
    LoggedInUser:'User' = None
    Users:List[dict] = []

    def __init__(self, username:str="", password:str="") -> None:
        # Loading Users From Memory (only gets run on the first instance the class is called)
        if User.Users == []:
            with open("./data/UserPasswords.json", "r") as file:
                jsonData = json.load(file)

                for data in jsonData:
                    User.Users.append({
                        "username": data["username"], 
                        "password": data["password"],
                    })

        self.username = username
        self.password = password
    
    # PRIVATE METHODS
    def _userExists(self, username: str) -> bool:
        for user in User.Users:
            if user["username"] == username:
                return True
        return False
        
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
        self.password = sha256(password.encode()).hexdigest()

        # Updating Users List
        User.Users.append({"username": self.username, "password": self.password})

        # Updating users.json
        with open("./data/UserPasswords.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
      
        data.update({"username": self.username, "password": self.password})

        with open("./data/UserPasswords.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    """ Public facing method which logs in a user (throws IncorrectPassword exceptions) """
    def login(self, password: str) -> bool:
        if self.password == sha256(password.encode()).hexdigest() and (self._userExists(self.username) or self.username == "developer" or self.username == "instructor"):
            User.LoggedInUser = self
        raise IncorrectPassword(self.username, password)
    

    """ Public facing method which loads an existing user and their password to log into (throws UserNotFound exception)"""
    def loadUser(self, username: str) -> None:
        for user in User.Users:
            if user["username"] == username:
                self.username = username
                self.password = user["password"]
                return
        raise UserNotFound(username)


    """ Public facing method which logs out a user """
    def logout(self) -> None:
        User.LoggedInUser = None
        self.username = ""
        self.password = ""
 