import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from user import User

class UserTest(unittest.TestCase):

    # -----------------------------------------------------------
    # When: A user object is created with name and symbol
    # Then: it creates a user object and returns it
    # -----------------------------------------------------------
    def test_user_creation(self):
        user = User('raghav', 'X')
        self.assertIsNotNone(user)

    # -----------------------------------------------------------
    # Given: A user object is created with name and symbol
    # When: User name is requested
    # Then: It returns the user name
    # -----------------------------------------------------------
    def test_user_name(self):
        user = User('raghav', 'X')
        self.assertEqual('raghav', user.getName())

    # -----------------------------------------------------------
    # Given: A user object is created with name and symbol
    # When: User symbol is requested
    # Then: It returns the user symbol
    # -----------------------------------------------------------
    def test_user_symbol(self):
        user = User('raghav', 'X')
        self.assertEqual('X', user.getSymbol())

if __name__ == '__main__':
    unittest.main()