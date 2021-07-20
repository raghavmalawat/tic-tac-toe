import socket
import user from User

class SocketClient(object):

    def __init__(self):
        # self.user = user
        self.server_host = "127.0.0.1"
        self.server_port = 8889
        self.server = socket.socket()
        self.user

    def connectToServer(self):
        self.server.connect((self.server_host, self.server_port))
        name = input("Enter the name of the first user 😀 : ")
        symbol = input("Enter the symbol of the first user 🔠 : ")
        self.user = User(name, symbol)
        self.sendCoordinatesToServer()



    def sendCoordinatesToServer(self, coordinate):
        self.server.send(coordinate.encode())

    # def sendMessageToServer(self):

    def listenMessageFromServer(self):
        while 1:
            data = self.server.recv(1024).decode()
            print(data)
            # we should get the coordinates and make corresponding action in the game

    def closeConnection(self):
        self.server.close()

          
if __name__ == '__main__':
    server = SocketClient()
    server.connectToServer()
    server.sendCoordinatesToServer("11")
    # server.listenMessageFromServer()
    # server.closeSocketServer()

