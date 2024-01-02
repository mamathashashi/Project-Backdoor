import socket
import os

#this is used to bind and accept connections
sockObject=socket.socket()
hostIP = "192.168.1.11"
portNumber = 8080
sockObject.bind((hostIP, portNumber))
sockObject.listen(1)
print(hostIP)
print("waiting for connections..")
conn, addr=sockObject.accept()
print("got connection!!")

filename=input(str("please enter the filename of the file:"))
file=open(filename, 'rb')
file_data=file.read(1024)
conn.send(file_data)
print("data has been transmitted successfully!")


#Execution of the Scripts
print("Enter h for help and q for exit")
while True:
    command = input(" >> ")
    conn.send(command.encode())
    if command == "q":
        print("Exiting Program!!!!")
        break

    elif command == "h":
        print("cd {path} --> to change directory")
        print("ls --> for listing contents of a directory")
        print("pwd --> to print present working directory")
        print("bash --> to execute shell scripts")
        print("clear --> to clear screen")

        
    elif command == "ls":
        result = conn.recv(1024).decode()
        print(result)

    elif command == "pwd":
        result = conn.recv(1024).decode()
        print(result)

    elif command == "clear":
        os.system("clear")

    elif command == "cd":
        print("command format is cd {path}")
        result = conn.recv(1024).decode()
        print(decode)

    elif command == "bash":
        os.system("clear")
        result = conn.recv(1024).decode()
        print(result)
        while True:
            execution = input("$$$")
            conn.send(execution.encode())
            result = conn.recv(1024).decode()
            print(result)
                                       
