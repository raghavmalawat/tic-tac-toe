import socket
import game from Game
import user from User

class ServerSocket(object):

    def __init__(self, port):
        self.server = socket.socket()
        self.port = port
        self.client1 = None
        self.client2 = None
        self.game = None

    def initializeServer(self):
        self.server.bind(('127.0.0.1', self.port))    
        self.server.listen(2) 
        print("Socket Server running on", self.port)
    
    def initializeClientConnection(self):
        while 1:
            client, address = self.server.accept()
            userData = client.recv(1024).decode()
            user = User(userData.split(' ')[0], userData.split(' ')[1])

            # get user details and initialize User
            if self.client1:
                self.client2 = client
                self.user2 = user
                self.game = Game(self.user1, self.user2)
                
                break
            else:
                self.client1 = client
                self.user1 = user
                break

    def receiveMessages(self):
        while 1:
            dataClient1 = self.client1.recv(1024).decode()
            print("Data from client 1", dataClient1)

            if (dataClient1):
                self.client2.send(dataClient1.encode())
                # make the move on behalf of A

            
        
            dataClient2 = self.client2.recv(1024).decode()
            print("Data from client 2", dataClient2)

            if (dataClient2):
                self.client1.send(dataClient2.encode())
                # make the move on behalf of A


    def closeSocketServer(self):
        for client in self.clients:
            client.close()
        print("Socket Server closed")
           
if __name__ == '__main__':
    server = ServerSocket(8889)
    server.initializeServer()
    server.initializeClientConnection()
    server.startGame()
    server.receiveMessages()
    # server.closeSocketServer()

