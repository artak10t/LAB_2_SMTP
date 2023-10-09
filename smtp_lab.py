from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.freesmtpservers.com", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
print ("Connecting to socket")
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailfromCommand = 'MAIL FROM: <spartak.gevorgyan@sjsu.edu>\r\n'
clientSocket.send(mailfromCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Send RCPT TO command and print server response.
rcpttoCommand = 'RCPT TO: <spartak.gevorgyan@sjsu.edu>\r\n'
clientSocket.send(rcpttoCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Send Subject command and print server response.
rcpttoCommand = 'SUBJECT: Hello\r\n'
clientSocket.send(rcpttoCommand.encode())

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)