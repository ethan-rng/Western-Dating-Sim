"""
Module: test_dev
Author: Jasper Yang
This module provides unit tests for the Developer class.

"""

from models.User import User
from models.Player import Player
from models.Developer import Developer
from typing import List
import json
import os
from models.exceptions import UserNotFound
import unittest

class TestDev(unittest.TestCase):
    """
    Unit tests for the Developer class.
    """

    def test_jumpto_screen(self):
        """
        Tests jump to screen function.
        """
        # Sign in to developer dashboard
        dev = Developer("abcd")
        # Test jump screen function to an actual screen
        dev.jumpToScreen(4)
        self.assertEqual(dev.level, 4)
        # Test out of bounds
        self.assertRaises(IndexError, dev.jumpToScreen, 8)
        self.assertRaises(IndexError, dev.jumpToScreen, 0)

if __name__ == '__main__':
    unittest.main()
