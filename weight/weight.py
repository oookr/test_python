# import sys
# import os
# import math
# from tkinter import * 
# from PIL import ImageTk, Image

# root = Tk()
# root.title('Your weight')
# root.geometry('800x600')

# photo = PhotoImage(file="dumtss.jpg")
# label = Label(image=photo)
# label.pack()


# canvas = Canvas(root, width=801, height=601, bg='#007')

# canvas.pack()
# root.mainloop()



# growth = input ("Enter the growth: ")
# growth = float(growth)
# resg =  (growth - 100) * 0.9
# print(resg)
# weight = input("Enter your weight: ")
# resg= float(resg); weight = float(weight)
# end = resg - weight 
# print ("#1 End =", end)
# # end *= -1
# if end >= 2.5:
# 	print ("You should have podnabrat weight",  end)
# elif end <= -2.5:
# 	print("You should've lost weight on ", end )
# else:
# 	print("Your weight is normal if you are fifty years old fat.")
# print ("#2 End =", end)
# Simple enough, just import everything from tkinter.
from tkinter import *
from PIL import Image, ImageTk


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        edit.add_command(label="button", command=self.button1)

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("chat.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=110, y=50)


    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def button1(self):
    	button = Button(self, text="Click ME!")
    	button.pack()
    	# button.grid(column=0, row=1)
        

    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  