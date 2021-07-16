import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from board import Board

class BoardTest(unittest.TestCase):

    def test_board_rows(self):
        board = Board()
        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]

        expected_rows = [['a', 'b', 'c'],
                            ['d', 'e', 'f'],
                            ['g', 'h', 'i']]

        self.assertEqual(expected_rows, board.rows)

    def test_board_columns(self):
        board = Board()
        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]

        expected_columns = [['a', 'd', 'g'],
                            ['b', 'e', 'h'],
                            ['c', 'f', 'i']]

        self.assertEqual(expected_columns, board.columns)
    
    def test_board_diagonals(self):
        board = Board()

        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]

        expected_diagonals = [['a', 'e', 'i'], ['c', 'e', 'g']]

        self.assertEqual(expected_diagonals, board.diagonals)

if __name__ == '__main__':
    unittest.main()