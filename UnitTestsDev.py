from models.User import User
from models.Player import Player
from models.Developer import Developer
from typing import List
import json, os
from models.exceptions import UserNotFound
import unittest

class testDev(unittest.TestCase):
    
    '''test jump to screen'''
    def test_jumptoScreen(self):
        #sign in to developer dashboard
        Dev: Developer = Developer("abcd")
        #test jumpscreen function to an actual screen
        Dev.jumptoScreen(4)
        self.assertEqual(Dev.level, 4)
        #test out of bounds
        self.assertRaises(IndexError, Dev.jumptoScreen, 8)
        self.assertRaises(IndexError, Dev.jumptoScreen, 0)


if __name__ == '__main__':
    unittest.main()