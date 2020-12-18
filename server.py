# UDP Server
from socket import *
import sys
SEGMENT_SIZE = 101


def main():
    if len(sys.argv) < 3:
        print("Too few arguments!")
        return

    UDPListenPort = sys.argv[1]
    TCPListenPort = sys.argv[2]
    TCP(TCPListenPort)
    UDP(UDPListenPort)


def UDP(serverPort):

    serverPort = int(serverPort)
    server_send_socket = socket(AF_INET, SOCK_DGRAM)

    server_send_socket.bind(("", serverPort))
    
    print("The server is ready to receive")
    while True:
        message, clientAddress = server_send_socket.recvfrom(1024)
        modifiedMessage = "I got your message"
        print("after receiving before sending")
        server_send_socket.sendto(modifiedMessage.encode(), clientAddress)
        print("after sending")

    return


def TCP(serverPort):
    # TCP Server
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = int(serverPort)
    serverSocket.bind(('', serverPort))
    # enter listening mode
    serverSocket.listen(1)
    chunk = ''
    print('The server is ready to receive...')
    # wait for message

    while True:
        # wait until a client connects
        # conncetionSocket which is specific to the calling client
        #  will be used
        (connectionSocket, addr) = serverSocket.accept()
        # recieve exactly SEGMENT_SIZE data
        while True:
            sentence = connectionSocket.recv(1024).decode()
            if not sentence:
                break
            # write to a file, create and write if not exists
            chunk = chunk + sentence
        break

    print("server recieved")
    with open("received.txt", "w+") as w:
        w.write(chunk)
    connectionSocket.close()
    return


main()
