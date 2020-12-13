import socket
import tqdm
import os
import json
import sys

<<<<<<< HEAD
s = socket.socket()
print(f"Socket have succesffuly created")

host = "192.168.0.136"
port = 8888

s.bind((host,port))
print(f"Socket has binded to " + str(port))

BUFFER_SIZE = 4096

SEPARATOR = "<SEPARATOR>"

s.listen(5)
print(f"Socket is listening")

client_socket, address = s.accept()

print(f"{address} is connected.")

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)

filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for _ in progress:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))

client_socket.close()
=======

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

s = socket.socket()
host = "192.168.0.136"
port = 8888

print(f"Connecting to the {host} : {port}")
s.connect((host,port))
print("Connected")

filename = input("Enter the file name")
print("Filename: ", filename)
filesize = os.path.getsize(filename)

s.send(f"{filename}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
        for _ in progress:

            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
           	 break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

>>>>>>> 9572e68... lab5 client
s.close()
