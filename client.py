from socket import *
import sys
import struct
import time
import hashlib
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
    UDP(serverIP, UDPListenPort, UDPSenderPort)
    TCP(serverIP, TCPListenPort, TCPSenderPort)


def UDP(serverIP, UDPListenPort, UDPSenderPort):
    serverName = serverIP
    serverPort = int(UDPListenPort)
    # read file into the variable f
    # with -> no need to close/free (automatically handled)
    with open("transfer_file_UDP.txt") as f:
        whole = f.read()

    client_send_socket = socket(AF_INET, SOCK_DGRAM)

    offset = 0
    sequence = 0
    # if read segment is smaller inside while loop
    # we read whole file
    while offset < len(whole):
        if offset + SEGMENT_SIZE > len(whole):
            message = whole[offset:]
        else:
            message = whole[offset:offset+SEGMENT_SIZE]
        offset = offset + SEGMENT_SIZE

        # struct(bytes) time into the message and encode
        message = struct.pack("d", time.time()) + message.encode()
        # send message
        client_send_socket.sendto(message, (serverName, serverPort))

        # receive from server 
        # normally for ACK, SEQ -> rdt 
        # couldn't implement
        response, serverAddress = client_send_socket.recvfrom(1024)

    message = b''
    client_send_socket.sendto(message, (serverName, serverPort))

    client_send_socket.close()
    return


def TCP(serverIP, serverPort, clientTCPSenderPort):
    # read the file into the whole
    # with -> closed automaticall no need to call f.close()
    with open("transfer_file_TCP.txt") as f:
        whole = f.read()

    # TCP Client
    # AF_INET -> means IPv4
    # SOCK_STREAM -> means TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = int(serverPort)

    offset = 0
    # connect to the server
    clientSocket.connect((serverIP, serverPort))

    while offset < len(whole):  # there exists data to send
        # data to be sent is smaller than te segment size
        if offset + SEGMENT_SIZE > len(whole):
            message = whole[offset:]
        else:
            message = whole[offset:offset+SEGMENT_SIZE]

        offset = offset + SEGMENT_SIZE
        # message to be sent
        # SEGMENT_SIZE long + time
        # send data to the server
        byt = struct.pack("d", time.time()) + message.encode()
        clientSocket.send(byt)

        # if required, recv a message from the server

    # send empty message in order to imply sending done
    message = b''
    clientSocket.send(message)

    # file sent close connection
    clientSocket.close()
    return


main()
