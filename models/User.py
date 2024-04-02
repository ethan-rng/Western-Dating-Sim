"""
Module: user_model
Authors Ethan Rong, Jasper Yang
This module provides the User class for user management.

"""

from models.exceptions import DuplicateUser, UserNotFound, IncorrectPassword, AdminLevelAccount, IncorrectPrivilege
from typing import List
from hashlib import sha256
import os
import json

class User:
    """
    A class to represent user management.

    Attributes:
    - LoggedInUser: class variable representing the currently logged-in user
    - Users: class variable representing a list of users

    Methods:
    - __init__: initializes the User instance
    - _checkDev: protected helper function to check if a developer is logged in
    - _checkInstructor: protected helper function to check if an instructor is logged in
    - _checkPlayer: protected helper function to check if a player is logged in
    - userExists: public method to check if a user exists
    - createUser: public method to create a new user account
    - loadUser: public method to load an existing user
    - login: public method to log in a user
    - logout: public method to log out a user
    """

    LoggedInUser: 'User' = None
    Users: List[dict] = []

    def __init__(self) -> None:
        """
        Initializes the User instance.
        Loads users from memory (only runs on the first instance the class is called).
        """
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

    def _checkDev(self) -> None:
        """
        Protected helper function to check if a developer is logged in.
        Throws IncorrectPrivilege exception if not.
        """
        if User.LoggedInUser != "developer":
            raise IncorrectPrivilege

    def _checkInstructor(self) -> None:
        """
        Protected helper function to check if an instructor is logged in.
        Throws IncorrectPrivilege exception if not.
        """
        if User.LoggedInUser != "instructor" and User.LoggedInUser != "developer":
            raise IncorrectPrivilege

    def _checkPlayer(self) -> None:
        """
        Protected helper function to check if a player is logged in.
        Throws IncorrectPrivilege exception if not.
        """
        if User.LoggedInUser != self.username and User.LoggedInUser != "instructor" and User.LoggedInUser != "developer":
            raise IncorrectPrivilege

    def userExists(self, username: str) -> bool:
        """
        Public method to check if a user exists.

        Parameters:
        - username: the username to check

        Returns:
        - bool: True if the user exists, False otherwise
        """
        for user in User.Users:
            if user["username"] == username:
                return True
        return False

    def createUser(self, username, password) -> None:
        """
        Public method to create a new user account.

        Parameters:
        - username: the username of the new user
        - password: the password of the new user

        Raises:
        - AdminLevelAccount: if the username is "developer" or "instructor"
        - DuplicateUser: if the username already exists
        """
        if username == "developer" or username == "instructor":
            raise AdminLevelAccount

        if self.userExists(username):
            raise DuplicateUser(username)

        self.username = username
        self._password = sha256(password.encode()).hexdigest()

        User.Users.append({"username": self.username, "password": self._password})

        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

    def loadUser(self, username: str) -> None:
        """
        Public method to load an existing user.

        Parameters:
        - username: the username of the user to load

        Raises:
        - UserNotFound: if the user does not exist
        """
        found = False
        for user in User.Users:
            if user["username"] == username:
                self.username = username
                self._password = user["password"]
                return
                
        raise UserNotFound(username)

    def login(self, username: str, password: str) -> None:
        """
        Public method to log in a user.

        Parameters:
        - username: the username of the user to log in
        - password: the password of the user to log in

        Raises:
        - IncorrectPassword: if the provided password is incorrect
        """
        if username == "developer":
            print(User.Users[0]["password"] == sha256(password.encode()).hexdigest())
            if User.Users[0]["password"] == sha256(password.encode()).hexdigest():
                User.LoggedInUser = "developer"
                
        elif username == "instructor":
            if User.Users[1]["password"] == sha256(password.encode()).hexdigest():
                User.LoggedInUser = "instructor"
                
        elif self._password == sha256(password.encode()).hexdigest() and (
                self.userExists(username)):
            User.LoggedInUser = self
        else:
            raise IncorrectPassword(self.username, password)

    def logout(self) -> None:
        """
        Public method to log out a user.
        """
        User.LoggedInUser = None
        self.username = ""
        self._password = ""
