def ttt(buttons):
	import urllib.request
	
	if button1:
		path = 'https://www.btwin.com/en/img'
		name = 'cover.jpg'
		if '.' in name: 
			url = path + '/' + name
			# from random import randint
			# rand = randint(1, 99)
			# name = str(rand) + name 
			urllib.request.urlretrieve(url, name) 
			end('1')
		else:
			url = 'https://www.btwin.com/en/'
			urllib.request.urlretrieve(url, 'samthing.html')
			end('2') 
def end(self):
	from sys import exit

	text = 'Beginning file download with urllib...\n' + self
	exit(text)
if __name__ == '__main__':
	from tkinter import *

	tk = Tk()
	button1 = Button(tk,text='download',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button1))
	button1.grid(row=1,column=1)
	tk.mainloop()