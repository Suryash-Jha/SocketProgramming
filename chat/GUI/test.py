from tkinter import *
from threading import Thread
root= Tk()
def func():
    i=0
    while(i != 5):
        text= input()
        print(i)
        i= i+1
thread1= Thread(target=func)
thread1.start()
root.mainloop()