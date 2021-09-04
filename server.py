
#importing modules for socket creation and to execute over system
import socket
import sys


def create_socket():
    try:
        #declaring them globally
        global s
        global host
        global port
        host="192.168.1.105"                          #IP address of server
        port= 9999                                    #Port on which we want the communication to happen
        print("Socket Creation Started...")
        s= socket.socket()                            #Socket Created

        print("Socket Created.")

    except socket.error as msg:                      #if any error while socket creation then print it
        print("Socket Creation Error" + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))                             #Socket binded with the host IP and port
        s.listen(5)                                      #listens for upcoming connection after every 5 sec
    except socket.error as msg:
        print("Socket Error" + str(msg))
        bind_socket()                                     #calling this function again, if failed

def socket_accept():

    #s.accept() gives two outputs:
    #one of them is object of the client system which we are reffering here as "conn"
    #other(address) is a list of IP and port with which server was connected.

    conn, address= s.accept()
    print("Connection has been established "+ address[0]+ " "+ str(address[1]))
    send_command(conn)                                   # to send commands to the client's system
    conn.close()                                         #connection is closed

def send_command(conn):
    while True:                                         #infinite loop as we want multiple commands to be sent
        cmd= input()
        if cmd== 'quit':
            conn.close()
            s.close()
            sys.exit()                                   #closes the cmd window
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))                    #encoding command strings to bytes
            client_response= str(conn.recv(1024), "utf-8")        #recieving and decoding client's reponse in block of 1024 bytes
            print(client_response, end=" ")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()




