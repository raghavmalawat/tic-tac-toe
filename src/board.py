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

    def printBoard(self):
        tab = tt.Texttable()
        tab.header(['', 0, 1, 2])

        printableRows = copy.copy(self.rows)
        printableRows.insert(0, [0, 1, 2])

        for row in [item for item in map(list, zip(*printableRows))]:
            tab.add_row(row)

        return tab.draw()


    def updateBoard(self, player, coordinates):
        self.rows[coordinates[0]][coordinates[1]] = player

    
    def checkWin(self, symbols):
        lines = self.rows + self.columns + self.diagonals

        for line in lines:
            if (all(board_position == symbols[0] for board_position in line) or all(board_position == symbols[1] for board_position in line)):
                return 1
        return 0

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
