import socket
from game import Game
from user import User

class ServerSocket(object):

    def __init__(self, port):
        self.server = socket.socket()
        self.port = port
        self.client1 = None
        self.client2 = None
        self.game = None
        self.user1 = None
        self.user2 = None

    def initializeServer(self):
        self.server.bind(('127.0.0.1', self.port))    
        self.server.listen(2) 
        print("Socket Server running on", self.port)
    
    def initializeClientConnection(self):
        while 1:
            client, address = self.server.accept()
            userData = None
            while userData == None:
                userData = client.recv(1024).decode()
                print(userData)
            
            user = User(userData.split(' ')[0], userData.split(' ')[1])

            # get user details and initialize User
            if self.client1:
                self.client2 = client
                self.user2 = user
                self.game = Game()
                break
            else:
                self.client1 = client
                self.user1 = user

    def receiveMessages(self):
        while 1:
            dataClient1 = self.client1.recv(1024).decode()
            print("Data from client 1", dataClient1)

            if (dataClient1 and self.client2):
                self.client2.send(dataClient1.encode())
                # make the move on behalf of A

            dataClient2 = None
            if self.client2:
                dataClient2 = self.client2.recv(1024).decode()
                print("Data from client 2", dataClient2)

            if (dataClient2 and self.client1):
                self.client1.send(dataClient2.encode())
                # make the move on behalf of A


    def closeSocketServer(self):
        self.client1.close()
        self.client2.close()

        print("Socket Server closed")

    def startGame(self):
        player1 = "Name of first player is " + self.user1.getName() + " and symbol is " + self.user1.getSymbol()
        self.client1.send(player1.encode()) 
        self.client2.send(player1.encode()) 

        player2 = "Name of second player is " + self.user2.getName() + " and symbol is " + self.user2.getSymbol()
        self.client1.send(player2.encode()) 
        self.client2.send(player1.encode()) 

if __name__ == '__main__':
    server = ServerSocket(8888)
    server.initializeServer()
    server.initializeClientConnection()
    if (server.user1 and server.user2):
        server.startGame()
        server.receiveMessages()
    # server.closeSocketServer()

