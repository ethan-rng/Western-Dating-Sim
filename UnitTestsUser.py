"""
Module: test_user
Author: Jasper Yang
This module provides unit tests for the User class.

"""

from models.User import User
from models.exceptions import DuplicateUser, UserNotFound, IncorrectPassword, AdminLevelAccount
from hashlib import sha256
import json
import os
import unittest

class TestUser(unittest.TestCase):
    """
    Unit tests for the User class.
    """

    def test_create_user(self):
        """
        Tests the create user function.
        """
        # Create a user
        jasper = User()
        jasper.createUser("Jasper", "abcd")
        # Checks if the username and password are correct
        self.assertEqual(jasper.username, "Jasper")
        self.assertEqual(jasper._password, sha256("abcd".encode()).hexdigest())
        # Tries to create a duplicate to see if it will be rejected
        jasper2 = User()
        self.assertRaises(DuplicateUser, jasper2.createUser, "Jasper", "abcd")
        # Deletes Jasper from password
        for user in User.Users:
            if user["username"] == "Jasper":
                User.Users.remove(user)
                break
        # Update JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
       

    def test_load_user(self):
        """
        Tests the load User function.
        """
        # Creates a user
        ethan = User()
        ethan.createUser("Ethan", "abcd")
        # Loads the user
        ethan2 = User()
        ethan2.loadUser("Ethan")
        self.assertEqual(ethan2._password, sha256("abcd".encode()).hexdigest())
        # Attempts to load non-existent user
        ethan3 = User()
        self.assertRaises(UserNotFound, ethan3.loadUser, "Ethan3")
        # Deletes Ethan from password
        for user in User.Users:
            if user["username"] == "Ethan":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)

    def test_login_and_logout(self):
        """
        Tests the login and logout functions.
        """
        # Creates user
        jasmine = User()
        jasmine.createUser("Jasmine", "abcd")
        # Attempt to login with the wrong password
        aaron = User()
        aaron.loadUser("Jasmine")
        self.assertRaises(IncorrectPassword, aaron.login, "Jasmine", "a")
        # Login with correct password
        aaron.login("Jasmine", "abcd")
        self.assertEqual(aaron.LoggedInUser, aaron)
        self.assertEqual(aaron.LoggedInUser.username, "Jasmine")
        # Logout
        aaron.logout()
        self.assertNotEqual(aaron.LoggedInUser, aaron)
        # Deletes Jasmine from password
        for user in User.Users:
            if user["username"] == "Jasmine":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)


if __name__ == '__main__':
    unittest.main()

