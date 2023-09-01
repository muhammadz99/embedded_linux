#! /usr/bin/python3

#Write a program that asks the user to type a word and return him its reverse

from tkinter import *

task02 = Tk()
task02.title("Reverse String")
task02.geometry("500x500+300+300")
task02.resizable(False,False)

ReversedString = "Ahmed"

def reverse():
    reversed_string.config(text=string.get()[::-1])

label1 = Label(task02, width= 10, height= 2, text="Entry String")
label2 = Label(task02, width= 10, height= 2, text="Result")
string = Entry(task02,fg="black", bg="grey",width= 10)
bt1 = Button(task02, fg="black", bg="grey",width= 4, height= 1, text = "Reverse", command=reverse)
reversed_string = Label(task02, width= 10, height= 1,fg="black", text="")
print(ReversedString)
label1.place(x= 100,y=55)
label2.place(x= 100,y=100)
string.place(x=200,y=60)
bt1.place(x=200,y=150)
reversed_string.place(x=225,y=105)

task02.mainloop()