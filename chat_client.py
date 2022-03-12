from socket import *
import time

# Greeting Message
print('This is a chat client created by Patrick Godfrey.\n')
print('Be sure to note down the IP address of the server you\'re going to connect to.\n')

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

# Get address
serverAddress = input(str("Enter server address: "))

# Connect socket 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect((serverAddress, port))
print("Connected! It's your turn to chat!\n")

while True:
    # Send a message, /q closes the socket.
    send_message = input('<ME>: ')
    if send_message == '/q':
        print('You have closed the chatroom.')
        send_bytes = send_message.encode('UTF-8')
        serverSocket.send(send_bytes)
        break
    send_bytes = send_message.encode('UTF-8')
    serverSocket.send(send_bytes)
    
    # Receives a message
    recv_bytes = serverSocket.recv(1024)
    recv_message = recv_bytes.decode('UTF-8')
    if recv_message == '/q':
        print('Server has closed the chatroom.')
        break
    print('<SERVER>:', recv_message)


serverSocket.close()
print('Shutting down program in 5 seconds.')
time.sleep(5)