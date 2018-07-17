import random as r
from tkinter import*

tk=Tk()
tk.title("Randoming")
tk.geometry()

tops = Frame(tk, width = 50, height= 6,bd=4 ,bg="#85929E" , relief="raise")
tops.pack(side=TOP)

# def res

def btnEqual():
	global operator
	r.randint("from", "to")
	operator = res
	messagebox.showinfo("Result",res)

operator = ""
Input_from=StringVar()
Input_to=StringVar()
# Input_res=StringVar()



efrom = Entry(tops, bg="#34495E",textvariable=Input_from)
efrom.grid(row =1, column = 0)
to= Entry(tops, bg="#34495E",textvariable=Input_to)
to.grid(row =1, column = 1)

# res= Entry(tk, bg="red",textvariable=Input_res)
# res.grid(row =2, column = 0)


btn = Button(tops, text="generate", command=lambda:btnEqual(), height=8,width= 30, bg="#3498DB")
btn.grid(row = 3,columnspan=4)

tk.mainloop()