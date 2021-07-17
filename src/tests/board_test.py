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

    def test_update_board(self):
        board = Board()
            
        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]

        board.update_board("X", (1, 2))

        expected_rows = [['a', 'b', 'c'],
                         ['d', 'e', 'X'],
                         ['g', 'h', 'i']]

        self.assertEqual(expected_rows, board.rows)

    def test_check_win_row(self):
        board = Board()

        board.rows = [['X', 'X', 'X'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]
                    
        self.assertTrue(board.check_win)

        board.rows = [['a', 'b', 'c'],
                      ['X', 'X', 'X'],
                      ['g', 'h', 'i']]
                    
        self.assertTrue(board.check_win)

        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['X', 'X', 'X']]
                    
        self.assertTrue(board.check_win)
        


    def test_check_win_col(self):
        board = Board()

        board.rows = [['X', 'b', 'c'],
                      ['X', 'e', 'f'],
                      ['X', 'h', 'i']]
                    
        self.assertTrue(board.check_win)

        board.rows = [['a', 'X', 'c'],
                      ['d', 'X', 'f'],
                      ['g', 'X', 'i']]
                    
        self.assertTrue(board.check_win)

        board.rows = [['a', 'b', 'X'],
                      ['d', 'e', 'X'],
                      ['g', 'h', 'X']]
                    
        self.assertTrue(board.check_win)

    def test_check_win_diagonal(self):
        board = Board()

        board.rows = [['X', 'b', 'c'],
                      ['d', 'X', 'f'],
                      ['g', 'h', 'X']]
                    
        self.assertTrue(board.check_win)

        board.rows = [['a', 'b', 'X'],
                      ['d', 'X', 'f'],
                      ['X', 'h', 'i']]
                    
        self.assertTrue(board.check_win)


    def test_check_no_win(self):
        board = Board()

        board.rows = [['X', 'b', 'X'],
                      ['d', 'X', 'f'],
                      ['g', 'h', 'i']]
                    
        self.assertTrue(board.check_win)

        board.rows = [['X', 'b', 'c'],
                      ['d', 'X', 'f'],
                      ['X', 'X', 'i']]
                    
        self.assertTrue(board.check_win)


if __name__ == '__main__':
    unittest.main()