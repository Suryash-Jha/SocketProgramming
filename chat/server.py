import socket
def create_socket():
    global host
    global port
    global s
    host= "192.168.1.106"
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


create_socket()
bind_socket()
accept()