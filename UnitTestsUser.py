from models.User import User
from models.exceptions import DuplicateUser, UserNotFound, IncorrectPassword, AdminLevelAccount, IncorrectPrivilege
from hashlib import sha256
import json, os
import unittest

#unit tests for user Class
class testUser(unittest.TestCase):

    '''tests the create user function'''
    def test_createUser(self):
        #create a user
        Jasper:User = User()
        Jasper.createUser("Jasper", "abcd")
        #checks if the username and password are correct
        self.assertEqual(Jasper.username, "Jasper")
        self.assertEqual(Jasper._password, sha256("abcd".encode()).hexdigest())
        #tries to create a duplicate to see if it will be rejected
        Jasper2:User = User()
        self.assertRaises(DuplicateUser, Jasper2.createUser, "Jasper", "abcd")
        #deletes Jasper from password
        for user in User.Users:
            if user["username"] == "Jasper":
                User.Users.remove(user)
                break
        # Update JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
        #checks if attempt to create admin level accounts are rejected
        self.assertRaises(AdminLevelAccount, Jasper2.createUser, "developer", "abcd")
        self.assertRaises(AdminLevelAccount, Jasper2.createUser, "instructor", "abcd")

    '''test the load User function'''
    def test_loadUser(self):
        #creates a user
        Ethan:User = User()
        Ethan.createUser("Ethan", "abcd")
        #loads the user
        Ethan2:User = User()
        Ethan2.loadUser("Ethan")
        self.assertEqual(Ethan2._password, sha256("abcd".encode()).hexdigest())
        #attempts to load non-existent user
        Ethan3:User = User()
        self.assertRaises(UserNotFound, Ethan3.loadUser, "Ethan3")
        #deletes Ethan from password
        for user in User.Users:
            if user["username"] == "Ethan":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)
    
    '''Tests the login and logout functions'''
    def test_login_and_logout(self):
        #creates user
        Jasmine:User = User()
        Jasmine.createUser("Jasmine", "abcd")
        #attemp to login with the wrong password
        Aaron:User = User()
        Aaron.loadUser("Jasmine")
        self.assertRaises(IncorrectPassword, Aaron.login,"Jasmine", "a")
        #login wiht correct password
        Aaron.login("Jasmine","abcd")
        self.assertEqual(Aaron.LoggedInUser, Aaron)
        self.assertEqual(Aaron.LoggedInUser.username, "Jasmine")
        #logout
        Aaron.logout()
        self.assertNotEqual(Aaron.LoggedInUser, Aaron)
        #deletes Jasmine from password
        for user in User.Users:
            if user["username"] == "Jasmine":
                User.Users.remove(user)
                break
        # Updates the JSON file
        with open(os.path.join("models", "data", "UserPasswords.json"), 'w', encoding='utf-8') as file:
            json.dump(User.Users, file, indent=4)


if __name__ == '__main__':
    unittest.main()