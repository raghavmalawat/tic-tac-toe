import unittest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from board import Board

class BoardTest(unittest.TestCase):

    # -----------------------------------------------------------
    # Given: An initialized board 
    # When: Rows are set for the board
    # Then: The roes are set for the board
    # -----------------------------------------------------------
    def test_board_rows(self):
        board = Board()
        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]

        expected_rows = [['a', 'b', 'c'],
                            ['d', 'e', 'f'],
                            ['g', 'h', 'i']]

        self.assertEqual(expected_rows, board.rows)

    # -----------------------------------------------------------
    # Given: A board with rows initialized
    # When: Board columns are requested
    # Then: It returns the right columns for the board
    # -----------------------------------------------------------
    def test_board_columns(self):
        board = Board()
        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]

        expected_columns = [['a', 'd', 'g'],
                            ['b', 'e', 'h'],
                            ['c', 'f', 'i']]

        self.assertEqual(expected_columns, board.columns)
    
    # -----------------------------------------------------------
    # Given: A board with rows initialized
    # When: Board diagonals are requested
    # Then: It returns the right diagonals for the board
    # -----------------------------------------------------------
    def test_board_diagonals(self):
        board = Board()

        board.rows = [['a', 'b', 'c'],
                      ['d', 'e', 'f'],
                      ['g', 'h', 'i']]

        expected_diagonals = [['a', 'e', 'i'], ['c', 'e', 'g']]

        self.assertEqual(expected_diagonals, board.diagonals)

    # ---------------------------------------------------------------------
    # Given: A board with rows initialized
    # When: Board coordinate is requested to update
    # Then: It updates the board at that coordinate with the symbol passed
    # ---------------------------------------------------------------------
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

    # ---------------------------------------------------------------------
    # Given: A board with rows initialized where a combination by row is winning
    # When: request to check win for that board is made
    # Then: It returns 1 if any player is winning the game
    # ---------------------------------------------------------------------
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

    # ---------------------------------------------------------------------
    # Given: A board with rows initialized where a combination by column is winning
    # When: request to check win for that board is made
    # Then: It returns 1 if any player is winning the game
    # ---------------------------------------------------------------------
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

    # ---------------------------------------------------------------------
    # Given: A board with rows initialized where a combination by diagonal is winning
    # When: request to check win for that board is made
    # Then: It returns 1 if any player is winning the game
    # ---------------------------------------------------------------------
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


    # ---------------------------------------------------------------------
    # Given: A board with rows initialized where a combination of 
    #        rows, columns and diagonals is not winning
    # When: request to check win for that board is made
    # Then: It returns 1 if any player is winning the game
    # ---------------------------------------------------------------------
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

    # ---------------------------------------------------------------------
    # Given: A board initialized 
    # When: Request to get the coordinates by user input is made
    # Then: It returns a tuple of the coordinates in the board
    # ---------------------------------------------------------------------
    def test_get_coordinates(self):
        board = Board()
        
        input_coordinates = '01'
        expected_parsed_coordinates = (0, 1)

        self.assertEqual(expected_parsed_coordinates, board.getBoardCoordinates(input_coordinates))

        input_coordinates = '21'
        expected_parsed_coordinates = (2, 1)
        
        self.assertEqual(expected_parsed_coordinates, board.getBoardCoordinates(input_coordinates))


    # ---------------------------------------------------------------------
    # Given: A board initialized and a symbol set for a particular coordinate
    # When: Request to get the coordinates on the user's input for the set coordinates 
    # Then: It returns a ValueError for duplicate coordinates
    # ---------------------------------------------------------------------
    def test_get_duplicate_coordinates(self):
        board = Board()
        board.rows = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        self.assertRaises(ValueError, board.getBoardCoordinates, '00')

    # ---------------------------------------------------------------------
    # Given: A board initialized
    # When: Request to get the coordinates on the user's input for 
    # coordinates outside the board is requested 
    # Then: It returns a ValueError for out of bounds coordinates
    # ---------------------------------------------------------------------
    def test_get_outofbound_coordinates(self):
        board = Board()

        self.assertRaises(ValueError, board.getBoardCoordinates, '04')
        self.assertRaises(ValueError, board.getBoardCoordinates, '32')



if __name__ == '__main__':
    unittest.main()