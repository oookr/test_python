def ttt(buttons):
	import urllib.request
	if button1:
		url = 'https://www.keralatourism.org/images/picture/large/Munnar_the_magical_experience_of_nature_77.jpg'  
		urllib.request.urlretrieve(url, '/nature_77.jpg') 
		if 1:
			print('Beginning file download with urllib...')
			
if __name__ == '__main__':
	from tkinter import *
	tk = Tk()
	button1 = Button(tk,text='download',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button1))
	button1.grid(row=1,column=1)
	tk.mainloop()
