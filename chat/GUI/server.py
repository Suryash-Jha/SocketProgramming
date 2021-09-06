import socket
import os
import signal
import subprocess
def create_socket():
    global host
    global port
    global s
    host= "192.168.1.101"
    port= 6895
    s= socket.socket()

def bind_socket():
    global host
    global port
    global s
    s.bind((host, port))

    print(f"Socket bound with {host} {port} ")
    s.listen(5)

def accept():

    conn, address= s.accept()
    print("Connection has been established "+ address[0]+ " "+ str(address[1]))
    funct(conn)
    conn.close()


def funct(conn):
    while True:
        talk = input(">")
        conn.send(str.encode(talk))
        recvv = conn.recv(1030).decode("utf-8")
        print(recvv)
        if recvv == 'quit':
            s.close()
            command= "netstat -ano | findstr 6895"
            c= subprocess.Popen(command, shell= True, stdout= subprocess.PIPE, stderr= subprocess.PIPE, stdin= subprocess.PIPE)
            stdout, stderr= c.communicate()
            pid= int(stdout.decode().strip().split(' ')[-1])
            os.kill(pid, signal.SIGTERM)


create_socket()
bind_socket()
accept()

command = "netstat -ano | findstr 6895"
c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
stdout, stderr = c.communicate()
pid = int(stdout.decode().strip().split(' ')[-1])
os.kill(pid, signal.SIGTERM)