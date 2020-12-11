# UDP Server
from socket import *
import sys


def main():
    if len(sys.argv) < 3:
        print("Too few arguments!")
        return

    UDPListenPort = sys.arg[1]
    TCPListenPort = sys.arg[2]
    TCP()
    UDP()


def UDP():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind((", serverPort))
    print("The server is ready to revieve")
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    return


def TCP():
    # TCP Server
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    # enter listening mode
    serverSocket.listen(1)
    print 'The server is ready to receive'
    # wait for message
    while True:
        # wait until a client connects
        # conncetionSocket which is specific to the calling client
        #  will be used
        connectionSocket, addr = serverSocket.accept()

        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
    return


main()