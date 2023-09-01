#! /usr/bin/python3

# Make Squared SHAPE using 4 buttons and each button display different name

from tkinter import *

def UpButton():
    print("Up Button is Pressed")
def LeftButton():
    print("Left Button is Pressed")
def RightButton():
    print("Right Button is Pressed")
def DownButton():
    print("Down Button is Pressed")

task01 = Tk()
task01.title(" Squared Shape Buttons")
task01.geometry("500x500+300+300")
task01.resizable(False,False)
bt1 = Button(task01, fg="black", bg="grey",width= 10, height= 2, text = "Up", command=UpButton)
bt2 = Button(task01, fg="black", bg="grey",width= 10, height= 2, text = 'Left',command=LeftButton)
bt3 = Button(task01, fg="black", bg="grey",width= 10, height= 2, text = 'Right',command=RightButton)
bt4 = Button(task01, fg="black", bg="grey",width= 10, height= 2, text='Down',command=DownButton)

bt1.place(x=200,y=25)
bt2.place(x=95,y=70)
bt3.place(x=305,y=70)
bt4.place(x=200,y=115)

task01.mainloop()