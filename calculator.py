from tkinter import *



tk=Tk()
tk.title("Calculator")

text = Label(tk,text=" ", bg="#202020", fg="white",font=('Times 30 bold'),height=4,width=16)
text.grid(row=0,column=0)

button1 = Button(tk,text="1",font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button1.grid(row=4,column=0)

button2 = Button(tk,text='2',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button2.grid(row=4,column=1)

button3 = Button(tk,text='3',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button3.grid(row=4,column=2)

button4 = Button(tk,text='4',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button4.grid(row=3,column=0)

button5 = Button(tk,text='5',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button5.grid(row=3,column=1)

button6 = Button(tk,text='6',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button6.grid(row=3,column=2)

button7 = Button(tk,text='7',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button7.grid(row=2,column=0)

button8 = Button(tk,text='8',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button8.grid(row=2,column=1)

button9 = Button(tk,text='9',font=('Times 20 bold'),bg='#D9D9D9',fg='#0f0f0f',height=2,width=4)
button9.grid(row=2,column=2)

button10 = Button(tk,text="0",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=8)
button10.grid(row=5,column=0)

button11 = Button(tk,text=".",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=4)
button11.grid(row=5,column=2,)

button12 = Button(tk,text="=",font=('Times 20 bold'),bg='#F9790E',fg='white',height=2,width=4)
button12.grid(row=5,column=3)

button13 = Button(tk,text="+",font=('Times 20 bold'),bg='#FA7D0F',fg='white',height=2,width=4)
button13.grid(row=4,column=3)

button14 = Button(tk,text="-",font=('Times 20 bold'),bg='#F98410',fg='white',height=2,width=4)
button14.grid(row=3,column=3)

button15 = Button(tk,text="×",font=('Times 20 bold'),bg='#F88A11',fg='white',height=2,width=4)
button15.grid(row=2,column=3)

button16 = Button(tk,text="÷",font=('Times 20 bold'),bg='#F99212',fg='white',height=2,width=4)
button16.grid(row=1,column=3)

button17 = Button(tk,text="%",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=4)
button17.grid(row=1,column=2)

button18 = Button(tk,text="С",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=4)
button18.grid(row=1,column=0)

button19 = Button(tk,text="+/-",font=('Times 20 bold'),bg='#C0C0C0',fg='#0f0f0f',height=2,width=4)
button19.grid(row=1,column=1)

tk.mainloop()