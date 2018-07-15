import random as r
from tkinter import*

tk=Tk()
tk.title("Randoming")
tk.geometry("400x300")

efrom = Entry(tk,)
efrom.grid(row =1, column = 0)
eto= Entry(tk,)
eto.grid(row =0, column = 1)

btn = Button(tk, text="generate", height=10,width= 20)
btn.grid(row = 1,column=0)
#  r.randint("from", "to")

tk.mainloop()