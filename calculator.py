from tkinter import *

tk=Tk()
tk.title("Calculator")

tops = Frame(tk, width = 300, height= 20,bd=4 , relief="raise")
tops.pack(side=TOP)
below = Frame(tk, width = 300, height= 20,bd=4 , relief="raise")
below.pack(side=BOTTOM)

#==============================================================================================================================
def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClear():
	global operator
	operator = ""
	text_Input.set("")

def btnEqual():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator = ""
# def percent
# def PM ():
# 	global operator
# 	operator = operator+ str(* (-1))
# 	text_Input.set(operator)

operator = ""
text_Input=StringVar()

#==============================================================================================================================
# from tkinter import messagebox
# import sys
# txt = txtDisplay
# if txt == "∕0" or txt == "⁄0"  or txt == "÷0" or txt == "∶0":
# 	messagebox.showinfo("Error with zero",'You can not divide by zero !!!')
# 	sys.exit()


txtDisplay= Entry(tops, font= ('arial',18,'bold'), textvariable=text_Input, width= 21,bd=4 , justify='right')
txtDisplay.grid(row = 0, column = 0)

btn10 = Button(below, text="C",command=lambda:btnClear(), padx= 16, bg='#C0C0C0', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn10.grid(row=1, column=0)
# if text_Input != "":
# 	btn10 = Button(below,text="AC",command=lambda:btnClear(),padx=16,bg='#C0C0C0', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
# 	btn10.grid(row=1,column=0)
PM = Button(below, text="+/-",command=lambda:btnClick("*(-1)"), padx= 16, bg='#C0C0C0', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
PM.grid(row=1, column=1)
percent = Button(below, text="%",command=lambda:btnClick("%"), padx= 16, bg='#C0C0C0', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
percent.grid(row=1, column=2)
divide = Button(below, text="÷",command=lambda:btnClick("/"), padx= 16, bg='#F99212',fg='white',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
divide.grid(row=1, column=3)

btn7 = Button(below, text="7",command=lambda:btnClick(7), padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn7.grid(row=2, column=0)
btn8 = Button(below, text="8",command=lambda:btnClick(8), padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn8.grid(row=2, column=1)
btn9 = Button(below, text="9",command=lambda:btnClick(9), padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn9.grid(row=2, column=2)
multiply = Button(below, text="×",command=lambda:btnClick("*"), padx= 16, bg='#F88A11',fg='white',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
multiply.grid(row=2, column=3)

btn4 = Button(below, text="4", padx= 16,command=lambda:btnClick(4), bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn4.grid(row=3, column=0)
btn5 = Button(below, text="5", padx= 16,command=lambda:btnClick(5), bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn5.grid(row=3, column=1)
btn6 = Button(below, text="6", padx= 16,command=lambda:btnClick(6), bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn6.grid(row=3, column=2)
minus = Button(below, text="−",command=lambda:btnClick("-"), padx= 16, bg='#F98410',fg='white',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
minus.grid(row=3, column=3)

btn1 = Button(below, text="1",command=lambda:btnClick(1), padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn1.grid(row=4, column=0)
btn2 = Button(below, text="2",command=lambda:btnClick(2), padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn2.grid(row=4, column=1)
btn3 = Button(below, text="3",command=lambda:btnClick(3), padx= 16, bg='#D9D9D9', fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
btn3.grid(row=4, column=2)
plus= Button(below, text="+",command=lambda:btnClick("+"), padx= 16, bg='#FA7D0F',fg='white',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
plus.grid(row=4, column=3)

btn0= Button(below, text="0",command=lambda:btnClick(0), padx= 16,bg='#C0C0C0',fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=8)
btn0.place(x=0,y=280)
point= Button(below, text=".",command=lambda:btnClick("."), padx= 16,bg='#C0C0C0',fg='#0f0f0f',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2,justify='left')
point.grid(row=5, column=2)
equal= Button(below, text="=",command=lambda:btnEqual(), padx= 16, bg='#F9790E',fg='white',pady=1,bd=4 ,font=('arial', 16, 'bold'),height=2,width=2)
equal.grid(row=5, column=3)



tk.mainloop()