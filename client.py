# import socket lib
from socket import *
import sys
# get input for server name and port#
# do not forget to put 1 sec time limitation
SEGMENT_SIZE = 101


def main():
    if len(sys.argv) < 6:
        print("Too few arguments!")
        return

    serverIP = sys.argv[1]
    UDPListenPort = sys.argv[2]
    TCPListenPort = sys.argv[3]
    UDPSenderPort = sys.argv[4]
    TCPSenderPort = sys.argv[5]
    TCP(serverIP, TCPListenPort, TCPSenderPort)
    UDP(serverIP, UDPListenPort, UDPSenderPort)


def UDP(serverIP, UDPListenPort, UDPSenderPort):
    serverName = serverIP
    serverPort = int(UDPListenPort)
    # read file into the variable f
    # with -> no need to close/free (automatically handled)
    with open("transfer_file_UDP.txt") as f:
        whole = f.read()
        
    print(len(whole))
    client_send_socket = socket(AF_INET, SOCK_DGRAM)

    offset = 0

    while offset < len(whole):
        message = whole[offset:offset + SEGMENT_SIZE]
        offset += SEGMENT_SIZE
        print("before sending...")
        client_send_socket.sendto(message.encode(), (serverIP, serverPort))
        print("after sending before receiving..")
        modifiedMessage, serverAddress = client_send_socket.recvfrom(1024)
        print("after receiving.")
        print(modifiedMessage.encode())

    client_send_socket.close()
    return


def TCP(serverIP, serverPort, clientTCPSenderPort):
    # read the file into the whole
    with open("transfer_file_TCP.txt") as f:
        whole = f.read()

    # TCP Client
    # AF_INET -> means IPv4
    # SOCK_STREAM -> means TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # handshaking
    serverPort = int(serverPort)

    offset = 0
    clientSocket.connect((serverIP, serverPort))
    while offset < len(whole):  # there exists data to send
        # data to be sent is smaller than te segment size
        print("offset: ", offset)
        print("len(whole): ", len(whole))
        if offset + SEGMENT_SIZE > len(whole):
            message = whole[offset:]
        else:
            message = whole[offset:offset+SEGMENT_SIZE]

        offset = offset + SEGMENT_SIZE
        # message to be sent
        # SEGMENT_SIZE long
        print("client sending..")
        # send data to the server
        byt = message.encode()
        clientSocket.send(byt)
        # if required, recv a message from the server

    # file sent close connection
    clientSocket.close()
    return


main()
