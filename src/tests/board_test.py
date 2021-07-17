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

        board.updateBoard("X", (1, 2))

        expected_rows = [['a', 'b', 'c'],
                         ['d', 'e', 'X'],
                         ['g', 'h', 'i']]

        self.assertEqual(expected_rows, board.rows)

    def test_check_win_row(self):
        board = Board()

        board.rows = [['X', 'X', 'X'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))

        board.rows = [['a', 'b', 'c'],
                      ['X', 'X', 'X'],
                      ['g', 'h', 'i']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))

        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['X', 'X', 'X']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))


    def test_check_win_col(self):
        board = Board()

        board.rows = [['X', 'b', 'c'],
                      ['X', 'e', 'f'],
                      ['X', 'h', 'i']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))

        board.rows = [['a', 'X', 'c'],
                      ['d', 'X', 'f'],
                      ['g', 'X', 'i']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))

        board.rows = [['a', 'b', 'X'],
                      ['d', 'e', 'X'],
                      ['g', 'h', 'X']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))

    def test_check_win_diagonal(self):
        board = Board()

        board.rows = [['X', 'b', 'c'],
                      ['d', 'X', 'f'],
                      ['g', 'h', 'X']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))

        board.rows = [['a', 'b', 'X'],
                      ['d', 'X', 'f'],
                      ['X', 'h', 'i']]
                    
        self.assertEqual(1, board.checkWin(['X', 'O']))


    def test_check_no_win(self):
        board = Board()

        board.rows = [['X', 'b', 'X'],
                      ['d', 'X', 'f'],
                      ['g', 'h', 'i']]
                    
        self.assertEqual(0, board.checkWin(['X', 'O']))

        board.rows = [['X', 'b', 'c'],
                      ['d', 'X', 'f'],
                      ['X', 'X', 'i']]
                    
        self.assertEqual(0, board.checkWin(['X', 'O']))

    def test_get_coordinates(self):
        board = Board()
        
        input_coordinates = '01'
        expected_parsed_coordinates = (0, 1)

        self.assertEqual(expected_parsed_coordinates, board.getBoardCoordinates(input_coordinates))

        input_coordinates = '21'
        expected_parsed_coordinates = (2, 1)
        
        self.assertEqual(expected_parsed_coordinates, board.getBoardCoordinates(input_coordinates))

    def test_get_duplicate_coordinates(self):
        board = Board()
        board.rows = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        self.assertRaises(ValueError, board.getBoardCoordinates, '00')

    def test_get_outofbound_coordinates(self):
        board = Board()

        self.assertRaises(ValueError, board.getBoardCoordinates, '04')
        self.assertRaises(ValueError, board.getBoardCoordinates, '32')



if __name__ == '__main__':
    unittest.main()