from socket import *
import sys
import struct
import time
import hashlib
SEGMENT_SIZE = 101


def main():
    if len(sys.argv) < 3:
        print("Too few arguments!")
        return

    UDPListenPort = sys.argv[1]
    TCPListenPort = sys.argv[2]
    UDP(UDPListenPort)
    TCP(TCPListenPort)


def UDP(serverPort):

    serverPort = int(serverPort)
    server_send_socket = socket(AF_INET, SOCK_DGRAM)

    server_send_socket.bind(("", serverPort))
    # if no request in 10 secs, stop the process
    server_send_socket.settimeout(10)
    data = ''
    totalTime = 0
    number = 0
    avgTime = 0

    sequence = 0

    # Round-robin like architecture
    # wait infinitely(10 secs in this case) for an event
    while True:
        message, clientAddress = server_send_socket.recvfrom(1024)
        if message == b'':
            break
        # extract time from incoming package
        t = struct.unpack("d", message[:8])[0]
        avgTime = time.time() - t
        # first incoming data, start timer
        if number == 0:
            totalTime = t
        # count incoming packages
        number = number + 1
        # buffer for incoming messages
        data = data + message[8:].decode()
        # respponse message format
        # normally ACK, SEQ informations
        # but couldn't implement :(
        response = "I send you a message and hope for the best (:smiley:)"
        server_send_socket.sendto(response.encode(), clientAddress)

    # calculate total time (in secs) * 1000
    totalTime = (time.time() - totalTime) * 1000
    # calculate avg time (in secs) * 1000
    avgTime = (avgTime / number) * 1000
    print("UDP Packets Average Transmission Time: ", avgTime, " ms")
    print("UDP Communication Total Transmission Time: ", totalTime, " ms")
    print("UDP server recieved")
    with open("transfer_file_UDP.txt", "w+") as w:
        w.write(data)
    return


def TCP(serverPort):
    # create TCP socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = int(serverPort)
    # bind it with the given port number
    serverSocket.bind(('', serverPort))
    # enter listening mode listen for connection request
    serverSocket.listen(1)
    # after 10 sec, no connection request close the server
    serverSocket.settimeout(10)
    # data read will be written in this
    chunk = ''
    avgTime = 0
    totalTime = 0
    number = 0

    # wait for message
    while True:
        # wait until a client connects
        # conncetionSocket which is specific to the calling client
        # will be used
        (connectionSocket, addr) = serverSocket.accept()
        # 101(SEGMENT_SIZE) + 8 (time) = read 109 byte
        while True:
            sentence = connectionSocket.recv(109)
            # eof indications
            if sentence == b'':
                break

            # extract time from incoming message
            t = struct.unpack("d", sentence[0:8])[0]
            # calculate time
            avgTime += time.time() - t
            # if it is the first incoming packet start totalTime timer
            if number == 0:
                totalTime = t
            # increment number to calculate avgTime
            number = number + 1
            # extract incoming data and decode
            # store in the buffer
            chunk = chunk + sentence[8:109].decode()
        break

    # calculate total time (in secs) * 1000
    totalTime = (time.time() - totalTime) * 1000
    # calculate avg time (in secs) * 1000
    avgTime = (avgTime / number) * 1000
    print("TCP Packets Average Transmission Time: ", avgTime, " ms")
    print("TCP Communication Total Transmission Time: ", totalTime, " ms")
    print("TCP server recieved")
    # open a file named TCPreceived -> "w+" option write, create if not exist
    with open("transfer_file_TCP.txt", "w+") as w:
        w.write(chunk)
    # close the connection
    connectionSocket.close()
    return


main()
