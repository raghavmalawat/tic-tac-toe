import itertools
from board import Board
from user import User
import time
class Game(object):

    def __init__(self):
        self.user1 = None
        self.user2 = None
        self.board = None

    def initializeBoard(self):
        self.board = Board()
        print ('-------------------------------------\n')
        print ('             TIC-TAC-TOE             \n')
        print ('-------------------------------------\n')

        print(self.board.printBoard())

    # take user names and symbols and prompt
    # user 2 to choose a different symbol if chosen otherwise
    def getUserInputs(self):
        name1 = input("Enter the name of the first user 😀 : ")
        symbol1 = input("Enter the symbol of the first user 🔠 : ")

        name2 = input("\nEnter the name of the second user 😀 : ")

        while True:
            try:
                symbol2 = input("Enter the symbol of the second user 🔠 : ")
                if symbol1 == symbol2:
                    raise ValueError('Same symbol used, please use a different symbol! 🛑')

            except (ValueError, IndexError, KeyError):
                print('Same symbol used, please use a different symbol! 🛑')
                continue
            break


        self.user1 = User(name1, symbol1)
        self.user2 = User(name2, symbol2)

    # take user name and symbol
    def getSingleUser(self):
        name1 = input("Enter the name of the user 😀 : ")
        symbol1 = input("Enter the symbol of the user 🔠 : ")

        symbol2 = 'X'
        if symbol1 == 'X':
            symbol2 = 'O'

        self.user1 = User(name1, symbol1)
        self.user2 = User('Computer', symbol2)

    # Play the game of tic tack toe between two players
    # Perform one operation at a time and check the board viability and 
    # if any user winning 
    def play(self):
        players = itertools.cycle([self.user1, self.user2])

        for x in range(9):
            player = next(players)

            if player.name == 'Computer':
                print ('\nComputer thinking its next move\n')
                time.sleep(2)
                coordinates = self.board.getComputerMove()
            else:
                print ('\n{} please enter the coordinates for your move'.format(player.getName()))

                while True:
                    try:
                        input_coordinates = input()
                        coordinates = self.board.getBoardCoordinates(input_coordinates)
                    except (ValueError, IndexError, KeyError):
                        print('\nThe coordinates you entered are not valid. Re-enter. 🛑')
                        continue
                    break

            self.board.updateBoard(player.getSymbol(), coordinates)
            print(self.board.printBoard())

            if x > 3:         # checking only when minimum of 5 operations are carried out 3 for A and 2 for B
                if self.board.checkWin([self.user1.getSymbol(), self.user2.getSymbol()]) == 1:
                    print('\n{} won! 🎉🔥'.format(player.getName()))
                    return

        print('\nThe game ended in a draw ☮️')


if __name__ == '__main__':
    game = Game()
    play = 1
    while play == 1:
        game.initializeBoard()
        singlePlayer = int(input("\nPress 1 for Single Player\nPress 2 for dual player mode\n"))
        if singlePlayer == 2:
            game.getUserInputs()
        else:
            game.getSingleUser()
        game.play()

        play = int(input("\nDo you want to play again? \nIf YES press 1, If NO press 0\n"))
