import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from user import User

class UserTest(unittest.TestCase):

    def test_user_creation(self):
        user = User('raghav', 'X')

        self.assertIsNotNone(user)

    def test_user_name(self):
        user = User('raghav', 'X')
        
        self.assertEqual('raghav', user.getName())

    def test_user_symbol(self):
        user = User('raghav', 'X')
        
        self.assertEqual('X', user.getSymbol())

if __name__ == '__main__':
    unittest.main()