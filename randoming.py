import random as r
import sys

def check_int(s):
	try:
		return int(s)
	except:
		print('please enter an integer!')
		sys.exit()

def check_str(x):
	try:
		return str(x)
	except:
		print('please enter an string!')
		sys.exit()
	
# №1
print ("How many numbers?")
num_str = input()
num = check_int(num_str)

if num > 100: # стереть num = int(input ()) и поставить if int(num) > 100: (str)	
	while num > 100 :
		if num > 100:
			print ("Number >  100, enter the number < 100")
			print ("How many numbers?")
		num_str = input ()
		num = check_int(num_str)
		if num <= 100:	
			print ("Your result:")
			for i in range(num):
				print( r.randint(0, 1))
	pass
elif num <= 100:
	print ("Your result:")
	for i in range(num):	
		
		print( r.randint(0, 1))
else:
	print("Error/Ошибка (report it/сообщите о ней)") 

# №2
tet_questionable = input("Do you want to have fun? (y or n) ")
tet = check_str(tet_questionable) 

if tet == "n":
	print(':(')
elif  tet == "y":
	while tet == "y" :
		
		for i in range(1):	
			print( r.randint(0, 1))

elif tet != "y" and tet != "n": 
	while tet != "y" and tet != "n":
		tet = str(input("|y or n| "))
		if tet == "n":
			print(':(')
		while tet == "y":
			if  tet == "y":
				for i in range(1): #!!!STOP program "Ctrl + C"!!!
					print( r.randint(0, 1))					
	pass	
else:
	print("Error/Ошибка (report it/сообщите о ней)")

