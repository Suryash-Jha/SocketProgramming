import socket
from tkinter import *
from threading import Thread

def talkwidget():
    Lab= Label(text= f"{recvv}").pack()
root = Tk()
root.geometry("400x400")

s= socket.socket()
host= "192.168.1.101"
port= 6895
s.connect((host, port))

def Chat():
    print("Welcome to Chat"+"\n")
    while True:
        global recvv
        recvv= s.recv(1030).decode("utf-8")
        talkwidget()
        print(recvv)
        talk= input(">")
        s.send(str.encode(talk))
        if recvv== 'quit':
            s.close()
        root.after(1000, Chat)
    print("---END---")

Thread1= Thread(target=Chat)
Thread1.daemon= True
Chat()
root.mainloop()




