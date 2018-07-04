from tkinter import *

tk=Tk()
tk.title("Calculator")

tops = Frame(tk, width = 300, height= 20, bd=4, relief="raise")
tops.pack(side=TOP)
below = Frame(tk, width = 300, height= 20, bd=4, relief="raise")
below.pack(side=BOTTOM)

txtDisplay= Entry(tops, font= ('arial',18,'bold'), width= 20, bd=4, justify='right')
txtDisplay.grid(row = 0, column = 0)


# from tkinter import messagebox
# import sys
# txt = txtDisplay
# if txt == "∕0" or txt == "⁄0"  or txt == "÷0" or txt == "∶0":
# 	messagebox.showinfo("Error with zero",'You can not divide by zero !!!')
# 	sys.exit()


btn10 = Button(below, text="C", padx= 16, bg='#C0C0C0', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=1, column=0)

PM = Button(below, text="+/-", padx= 16, bg='#C0C0C0', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=1, column=1)

percent = Button(below, text="%", padx= 16, bg='#C0C0C0', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=1, column=2)

divide = Button(below, text="÷", padx= 16, bg='#F99212',fg='white',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=1, column=3)
#=========================================================================

btn7 = Button(below, text="7", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=2, column=0)

btn8 = Button(below, text="8", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=2, column=1)

btn9 = Button(below, text="9", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=2, column=2)

multiply = Button(below, text="×", padx= 16, bg='#F88A11',fg='white',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=2, column=3)
#=========================================================================

btn4 = Button(below, text="4", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=3, column=0)

btn5 = Button(below, text="5", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=3, column=1)

btn6 = Button(below, text="6", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=3, column=2)

minus = Button(below, text="−", padx= 16, bg='#F98410',fg='white',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=3, column=3)
#=========================================================================

btn1 = Button(below, text="1", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=4, column=0)

btn2 = Button(below, text="2", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=4, column=1)

btn3 = Button(below, text="3", padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=4, column=2)

plus= Button(below, text="+", padx= 16, bg='#FA7D0F',fg='white',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=4, column=3)
#=========================================================================

btn0= Button(below, text="0", padx= 16,bg='#C0C0C0',fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=8).place(x=-1,y=280)

# btn00= Button(below, text="0", padx= 16,bg='#C0C0C0',fg='#0f0f0f',pady=1,
# 				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=5, column=1)

point= Button(below, text=".", padx= 16,bg='#C0C0C0',fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2,justify='left').grid(row=5, column=2)

equal= Button(below, text="=", padx= 16, bg='#F9790E',fg='white',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=5, column=3)
#=========================================================================



tk.mainloop()