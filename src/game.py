import itertools
from board import Board
from user import User

class Game(object):

    def __init__(self):
        self.user1 = None
        self.user2 = None
        self.board = None

    def initializeBoard(self):
        self.board = Board()

    def getUserInputs(self):
        name1 = input("Enter the name of the first user : ")
        symbol1 = input("Enter the symbol of the first user : ")

        name2 = input("\nEnter the name of the second user : ")

        while True:
            try:
                symbol2 = input("Enter the symbol of the second user : ")
                if symbol1 == symbol2:
                    raise ValueError('Same symbol used, please use a different symbol!')

            except (ValueError, IndexError, KeyError):
                print('Same symbol used, please use a different symbol!')
                continue
            break


        self.user1 = User(name1, symbol1)
        self.user2 = User(name2, symbol2)


    def play(self):
        players = itertools.cycle([self.user1, self.user2])
        print(self.board.printBoard())

        for x in range(9):
            player = next(players)
            print ('\n{} please enter the coordinates for your move'.format(player.getName()))

            while True:
                try:
                    input_coordinates = input()
                    coordinates = self.board.getBoardCoordinates(input_coordinates)
                except (ValueError, IndexError, KeyError):
                    print('\nThe coordinates you entered are not valid. Re-enter.')
                    continue
                break

            self.board.updateBoard(player.getSymbol(), coordinates)
            print(self.board.printBoard())

            if x > 3:
                if self.board.checkWin([self.user1.getSymbol(), self.user2.getSymbol()]) == 1:
                    print('\n{} won!'.format(player.getName()))
                    return

        print('\nThe game ended in a draw')


if __name__ == '__main__':
    game = Game()
    game.initializeBoard()
    game.getUserInputs()
    game.play()