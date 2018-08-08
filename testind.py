import sys
import subprocess
from import_my import check_int
from import_my import check_str2

#The game guess what a word
# check_num = ["1","2","3","4","5","6","7","8","9","0"]

a = input ("Enter the word: ")
# mathe=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
a = check_str2(a)
if ("joke")in a:
	imgJoke = r'start chrome file:///D:/small_work/python_test/img/dumtss.jpg'	
	#this program assumes that you have a chrome
	subprocess.Popen(imgJoke,shell = True)
	sys.exit()
# elif mathe in a :
# 	print("Hey what's up?")
# 	# while :
# 	sys.exit()
elif ("google") in a or ("google.com") in a:
	google = r'start chrome /new-tab'	
	#this program assumes that you have a chrome
	subprocess.Popen(google,shell = True)
	sys.exit()
b = input ("What kind of letter do you need?")
b = check_int(b) 
if (":") in b:
	print("Hey what's up?")
	# while :
	sys.exit()

