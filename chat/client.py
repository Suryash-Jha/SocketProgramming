import socket
s= socket.socket()
host= "192.168.1.105"
port= 6895
s.connect((host, port))

print("Welcome to Chat"+"\n")
name= input("Enter Your Name:")
s.send(str.encode(name))

while True:

    recvv= s.recv(1030).decode("utf-8")
    print(recvv)
    talk= input(">")
    s.send(str.encode(talk))
    if recvv== 'quit':
        s.close()


