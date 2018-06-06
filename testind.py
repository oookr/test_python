import sys
import subprocess
from import_my import check_int

#1
#BUGGG
# print as p 
num_1 = float(input ("Entet first num: "))
num_2 = float(input ("Entet second num: "))
res1 = float(num_1 + num_2)
print ("Result is one", res1)
res2 = float(num_1 + num_2 + res1)
print ("Result is two", res2)
res = float(res1 + res2)
print ("Sum of results", res) 

#2
#The game guess what a word
# check_num = ["1","2","3","4","5","6","7","8","9","0"]

a = input ("Enter the word: ")

if ("мамка")in a:
	mamka = r'start chrome file:///D:/small_work/python_test/img/dumtss.jpg'	
	#this program assumes that you have a chrome
	subprocess.Popen(mamka,shell = True)
	sys.exit()
elif ("1") in a or ("2") in a or ("3") in a or ("4") in a or ("5") in a or ("6") in a or ("7") in a or ("8") in a or ("9") in a or ("0") in a :
	print("Hey what's up?")
	# while :
	sys.exit()
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

