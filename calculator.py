from tkinter import *

# tk=Tk()
# tk.title("Calculator")

# text_Input=StringVar()

# text = Label(tk,text=" ", bg="#202020", fg="white",font=('Times 30 bold'),height=4,width=16)
# text.grid(row=0,column=0)

# txtDisplay = Entry(tk, font=('Times 30 bold'), textvariable=text_Input,
#                      bg="#202020", fg="white", justify='right' ).grid(columnspan=4)

# button1 = Button(tk,text="1",font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button1.grid(row=4,column=0)

# button2 = Button(tk,text='2',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button2.grid(row=4,column=1)

# button3 = Button(tk,text='3',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button3.grid(row=4,column=2)

# button4 = Button(tk,text='4',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button4.grid(row=3,column=0)

# button5 = Button(tk,text='5',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button5.grid(row=3,column=1)

# button6 = Button(tk,text='6',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button6.grid(row=3,column=2)

# button7 = Button(tk,text='7',font=('Times 20 bold'), bg='#D9D9D9', fg='#0f0f0f',height=2,width=2)
# button7.grid(row=2,column=0)

# button8 = Button(tk,text='8',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button8.grid(row=2,column=1)

# button9 = Button(tk,text='9',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=2)
# button9.grid(row=2,column=2)

# button10 = Button(tk,text="0",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=8)
# button10.grid(row=5,column=0)

# button11 = Button(tk,text=".",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=2)
# button11.grid(row=5,column=2,)

# button12 = Button(tk,text="=",font=('Times 20 bold'),bg='#F9790E',fg='white',height=2,width=2)	
# button12.grid(row=5,column=3)

# button13 = Button(tk,text="+",font=('Times 20 bold'),bg='#FA7D0F',fg='white',height=2,width=2)
# button13.grid(row=4,column=3)

# button14 = Button(tk,text="-",font=('Times 20 bold'),bg='#F98410',fg='white',height=2,width=2)
# button14.grid(row=3,column=3)

# button15 = Button(tk,text="×",font=('Times 20 bold'),bg='#F88A11',fg='white',height=2,width=2)
# button15.grid(row=2,column=3)

# button16 = Button(tk,text="÷",font=('Times 20 bold'),bg='#F99212',fg='white',height=2,width=2)
# button16.grid(row=1,column=3)

# button17 = Button(tk,text="%",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=2)
# button17.grid(row=1,column=2)

# button18 = Button(tk,text="С",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=2)
# button18.grid(row=1,column=0)

# button19 = Button(tk,text="+/-",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=2)
# button19.grid(row=1,column=1)

# tk.mainloop()

'''
"""
!!! http://www.newthinktank.com/2016/09/learn-program-22/
"""
'''

# cal = Tk()
# cal.title("Calculator")
# operator=""
# text_Input=StringVar()

# txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd =30, insertwidth=4,
#                      bg="#202020", fg="white", justify='right' ).grid(columnspan=4)
# #=========================================================================
# btn10 = Button(cal, text="C", padx= 16, bg='#C0C0C0', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=1, column=0)

# PM = Button(cal, text="+/-", padx= 16, bg='#C0C0C0', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=1, column=1)

# percent = Button(cal, text="%", padx= 16, bg='#C0C0C0', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=1, column=2)

# divide = Button(cal, text="÷", padx= 16, bg='#F99212',fg='white',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=1, column=3)
# #=========================================================================

# btn7 = Button(cal, text="7", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=2, column=0)

# btn8 = Button(cal, text="8", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=2, column=1)

# btn9 = Button(cal, text="9", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=2, column=2)

# multiply = Button(cal, text="×", padx= 16, bg='#F88A11',fg='white',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=2, column=3)
# #=========================================================================

# btn4 = Button(cal, text="4", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=3, column=0)

# btn5 = Button(cal, text="5", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=3, column=1)

# btn6 = Button(cal, text="6", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=3, column=2)

# minus = Button(cal, text="−", padx= 16, bg='#F98410',fg='white',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=3, column=3)
# #=========================================================================

# btn1 = Button(cal, text="1", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=4, column=0)

# btn2 = Button(cal, text="2", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=4, column=1)

# btn3 = Button(cal, text="3", padx= 16, bg='#D9D9D9', fg='#0f0f0f', 
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=4, column=2)

# plus= Button(cal, text="+", padx= 16, bg='#FA7D0F',fg='white',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=4, column=3)
# #=========================================================================

# btn0= Button(cal, text="0", padx= 16,bg='#C0C0C0',fg='#0f0f0f',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=5, column=0)

# btn00= Button(cal, text="0", padx= 16,bg='#C0C0C0',fg='#0f0f0f',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=5, column=1)

# point= Button(cal, text=".", padx= 16, bg='#F88A11', fg='white',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=5, column=2)

# equal= Button(cal, text="=", padx= 16, bg='#F9790E',fg='white',
# 				bd=8 ,font=('arial', 20, 'bold')).grid(row=5, column=3)
# #=========================================================================


# cal.mainloop()

tk=Tk()
tk.title("Calculator")

tops = Frame(tk, width = 300, height= 20, bd=4, relief="raise")
tops.pack(side=TOP)
below = Frame(tk, width = 300, height= 20, bd=4, relief="raise")
below.pack(side=BOTTOM)

txtDisplay= Entry(tops, font= ('arial',18,'bold'), width= 21, bd=4, justify='right')
txtDisplay.grid(row = 0, column = 0)

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
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=5, column=0)

btn00= Button(below, text="0", padx= 16,bg='#C0C0C0',fg='#0f0f0f',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=5, column=1)

point= Button(below, text=".", padx= 16, bg='#F88A11', fg='white',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=5, column=2)

equal= Button(below, text="=", padx= 16, bg='#F9790E',fg='white',pady=1,
				bd=4 ,font=('arial', 16, 'bold'),height=2,width=2).grid(row=5, column=3)
#=========================================================================



tk.mainloop()