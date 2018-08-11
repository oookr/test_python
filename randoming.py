from tkinter import *
from random import randint

tk=Tk()
tk.title("Randoming")
tk.geometry()

Input_from=StringVar()
Input_to=StringVar()

tops = Frame(tk, width = 50, height= 6,bd=4 ,bg="#85929E" , relief="raise")
tops.pack(side=TOP)
Label_from =Label(tops, text ="from:",bg="#85929E",)
Label_to=Label(tops, text ="to  :",bg="#85929E",)
Label_from.grid(row=1, column=0)
Label_to.grid(row=2, column=0)
Entry_from = Entry(tops, bg="#34495E",textvariable=Input_from)
Entry_to = Entry(tops, bg="#34495E",textvariable=Input_to)
Entry_from.grid(row =1, column = 1)
Entry_to.grid(row =2, column = 1)

def btnEqual():
	Nam_from = Entry_from.get()
	# Nam_from = int(Nam_from)
	Nam_to = Entry_to.get()
	# Nam_to = int(Nam_to)
	res = randint(Nam_from, Nam_to)
	# res = str(res)
	tk.messagebox.showinfo("Result", res)

btn = Button(tops, text="generate", command=btnEqual(), height=4,width= 15, bg="#3498db")
btn.grid(row = 3,columnspan=4)

tk.mainloop()

'''
import random as r
s = input("from : ")
ss= input("to   : ")
res = randint(int(s), int(ss))
print (res)
'''

"""
https://www.python-course.eu/tkinter_entry_widgets.php
https://metanit.com/python/tutorial/9.6.php
"""