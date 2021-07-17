import texttable as tt
import copy
class Board(object):

    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    @property
    def diagonals(self):
        return [[self.rows[0][0], self.rows[1][1], self.rows[2][2]],
                [self.rows[0][2], self.rows[1][1], self.rows[2][0]]]

    @property
    def columns(self):
        return [item for item in map(list, zip(*self.rows))]

    def __str__(self):
        return "  0 1 2\n0 {}\n1 {}\n2 {}".format(' '.join(self.rows[0]),
                                                  ' '.join(self.rows[1]),
                                                  ' '.join(self.rows[2]))

    # prints the gma eboard in a table format
    def printBoard(self):
        tab = tt.Texttable()
        tab.header(['', 0, 1, 2])

        printableRows = copy.deepcopy(self.rows)

        for i in range(len(self.rows)):
            printableRows[i].insert(0, i)

        for row in printableRows:
            tab.add_row(row)

        return tab.draw()


    def updateBoard(self, player, coordinates):
        self.rows[coordinates[0]][coordinates[1]] = player

    # Check if all the symbols for any row or column or diagonal matches
    # If yes, return true else return false
    def checkWin(self, symbols):
        lines = self.rows + self.columns + self.diagonals

        for line in lines:
            if (all(board_position == symbols[0] for board_position in line) or all(board_position == symbols[1] for board_position in line)):
                return 1
        return 0

    # Convert user input for coordinate to a tuple and if 
    # value already set or out of bounds return relevant error
    def getBoardCoordinates(self, inputCoordinates):
        try:
            coordinates = (int(inputCoordinates[0]), int(inputCoordinates[1]))
        except (ValueError):
            raise ValueError('Invalid coordinates')

        if (coordinates[0] >= (len(self.rows)) or coordinates[1] >= (len(self.columns))):
            raise ValueError('Out of bound coordinates')

        if self.rows[coordinates[0]][coordinates[1]] != ' ':
            raise ValueError('Duplicate coordinates')

        return coordinates
