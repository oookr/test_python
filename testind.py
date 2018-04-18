import sys
import subprocess
from import_my import check_int

#1
##BUGGG
## print as p 
# num_1 = float(input ("Entet first num: "))
# num_2 = float(input ("Entet second num: "))
# res1 = float(num_1 + num_2)
# print ("Result is one", res1)
# res2 = float(num_1 + num_2 + res1)
# print ("Result is two", res2)
# res = float(res1 + res2)
# print ("Sum of results", res) 

#2
# #In the "C" language, this would not work
# a = input("a: ")
# b = input("b: ")
# if a==b:
# 	print("yep")
# elif a!=b:
# 	print("nop")

#3
#The game guess what a word
import subprocess

a = input ("Enter the word: ")
# print (a[0:1])	
if ("mam") in a or ("Mam") in a  or ("Мам")in a or ("мам")in a:
	mamka = r'start chrome file:///D:/small_work/python_test/img/dumtss.jpg'
	subprocess.Popen(mamka,shell = True)
	sys.exit()
b = input ("What kind of letter do you need?")
if (":") in b :
	print("Hey what's up?")
