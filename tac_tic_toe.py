from tkinter import *
from tkinter import messagebox
from sys import exit

tk=Tk()
tk.title("Tic Tac Toe")

bclick = True
          
def ttt(buttons):
     WinX = ("Player X",'Winner is X !!!')
     global bclick
     if buttons['text'] == ' '  and bclick == True:
         buttons['text'] = 'X'
         bclick = False
     elif buttons['text'] == ' ' and bclick == False:
          buttons['text'] = 'O'
          bclick = True

     #If you see that you won then press the button twice
     elif(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'or
          button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'or
          button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
          messagebox.showinfo("Player X",'Winner is X !!!!')
          exit('Winner is X !!!!')
     elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          messagebox.showinfo("Player O",'Winner is O !!!!') 
          exit('Winner is O !!!!')

buttons=StringVar()

button1 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button1))
button1.grid(row=1,column=0)

button2 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button2))
button2.grid(row=1,column=1)

button3 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button3))
button3.grid(row=1,column=2)

button4 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button4))
button4.grid(row=2,column=0)

button5 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button5))
button5.grid(row=2,column=1)

button6 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button6))
button6.grid(row=2,column=2)

button7 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button7))
button7.grid(row=3,column=0)

button8 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button8))
button8.grid(row=3,column=1)

button9 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button9))
button9.grid(row=3,column=2)

tk.mainloop()