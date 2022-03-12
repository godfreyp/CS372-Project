from socket import *
import time

# Greeting Message
print('This is a chat server created by Patrick Godfrey.\n')
print('Please initilize this program first.\n')

# Get valid port
port = input("Please enter the port you wish to use: ")
if port.isnumeric() == True:
    if int(port) < 0 or int(port) > 65535:
        print("Invalid port!")
        port = ""
while port.isnumeric() != True:
    port = input("Please enter a valid port number: ")
    if port.isnumeric() == True:
        if int(port) < 0 or int(port) > 65535:
            print("Invalid port!")
            port = ""
    else:
        print("Invalid port!")
port = int(port)

# Create socket 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(("", port))
host = gethostname()
ip = gethostbyname(host)
print("Port:", port, " and IP Address:", ip)

# Await connections
serverSocket.listen(1)
print("\nWaiting for incoming connections...\n")
newsock, (remhost, remport) = serverSocket.accept()
print("Connection established with %s:%s\n" % (remhost, remport))

while True:
    # Receive a message
    bytes = newsock.recv(1024)
    recv_message = bytes.decode('UTF-8')
    if recv_message == '/q':
        print('Client has closed the chatroom.')
        break
    print("<CLIENT>:", recv_message)

    # Send a message, /q closes the socket
    send_message = input('<ME>: ')
    if send_message == '/q':
        print('You have closed the chatroom.')
        bytes = send_message.encode('UTF-8')
        newsock.send(bytes)
        break
    bytes = send_message.encode('UTF-8')
    newsock.send(bytes)

newsock.close()
print('Shutting down program in 5 seconds.')
time.sleep(5)