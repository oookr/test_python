def ttt(buttons):
	import urllib.request
	if button1:
		path = 'https://www.keralatourism.org/images/picture/large'
		name = 'Munnar_the_magical_experience_of_nature_77.jpg'
		if '.' in name: 
			url = path + '/' + name 
			urllib.request.urlretrieve(url, name) 
			end('1')
		else: #Don't worck
			url = path + '.html' 
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