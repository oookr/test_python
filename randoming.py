import random as r
from tkinter import*

tk=Tk()
tk.title("Randoming")
tk.geometry()

tops = Frame(tk, width = 50, height= 6,bd=4 ,bg="#85929E" , relief="raise")
tops.pack(side=TOP)
Input_from=StringVar()
Input_to=StringVar()
# def res
c =Label(tops, text ="from:",bg="#85929E",)
c.grid(row=1, column=0)
to=Label(tops, text ="to  :",bg="#85929E",)
to.grid(row=2, column=0)
ec = Entry(tops, bg="#34495E",textvariable=Input_from)
ec.grid(row =1, column = 1)
eto = Entry(tops, bg="#34495E",textvariable=Input_to)
eto.grid(row =2, column = 1)

def btnEqual():
	ec = int(ec)
	eto = int(eto) 
	res = r.randint(c, to)
	res = str(res)
	tk.messagebox.showinfo("Result", res)

# Input_res=StringVar()





btn = Button(tops, text="generate", command=lambda:btnEqual(), height=4,width= 15, bg="#3498db")
btn.grid(row = 3,columnspan=4)

tk.mainloop()

'''
import random as r
s = input("from : ")
ss= input("to   : ")
res = r.randint(int(s), int(ss))
print (res)
'''