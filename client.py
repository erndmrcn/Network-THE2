# A Simple Server-Client Application for tutorial
# UDP Client
# import socket lib
from socket import *
import sys
# get input for server name and port#
# do not forget to put 1 sec time limitation


def main():
    if len(sys.argv) < 6:
        print("Too few arguments!")
        return


def UDP():
    serverName = 'hostName'
    serverPort = 12000

    # create UDP socket for server
    # soc_dgram -> datagram -> means UDP
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # for this application we send input from stdin
    message = raw_input('Input lowercase sentence:')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # servername yo IP done in sendto by calling DNS
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print(modifiedMessage.decode())
    clientSocket.close()
    return


def TCP(serverIP, serverPort):
    with open("transfer_file_TCP.txt", "rb") as f:
        while bytearray := f.read(1000):
            print(bytearray)

    # TCP Client

    # AF_INET -> means IPv4
    # SOCK_STREAM -> means TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # handshaking
    serverPort = int(serverPort)
    clientSocket.connect((serverIP, serverPort))
    sentence = raw_input('Input lowercase sentence:')
    # since connection is already established instead
    # of sendto this time send
    # send 10 bytearray
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())
    clientSocket.close()
    return


main()
serverIP = sys.argv[1]
serverUDPListenPort = sys.argv[2]
serverTCPListenPort = sys.argv[3]
clientUDPSenderPort = sys.argv[4]
clientTCPSenderPort = sys.argv[5]
TCP(serverIP, serverTCPListenPort)

print(serverIP, serverUDPListenPort, serverTCPListenPort, clientUDPSenderPort, clientTCPSenderPort)
