import socket

s = socket.socket()
<<<<<<< HEAD
print("Berjaya buat sokett")

port = 8888

s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("soket tengah menunggu client!")

while True:
        c, addr = s.accept()
        print("Dapat capaian dari: " + str(addr))

        c.send(b'Terima Kasih!')
        buffer = c.recv(1024)
        print(buffer)
c.close()
=======

port = 8888

s.connect(('192.168.0.136', port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
>>>>>>> 9572e68... lab5 client
