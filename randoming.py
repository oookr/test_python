import random as r

from import_my import check_int
from import_my import check_str

# №1
print ("How many numbers?")
num_str = input()
num = check_int(num_str)

if num > 100: # стереть num = int(input ()) и поставить if int(num) > 100: (str)	
	while num > 100 :
		if num > 100:
			num = input ("Number >  100, enter the number < 100\nHow many numbers?\n")
			num = check_int(num)
		if num <= 100:	
			print ("Your result:")
			for i in range(num):
				print( r.randint(0, 1))
			print ("\n___Good___\n")
	pass

elif num <= 100:
	print ("Your result:")
	for i in range(num):	
		
		print( r.randint(0, 1))
	print ("\n___Good___\n")

else:
	print("Error/Ошибка") 


# №2
tet = input("\nDo you want to have fun? (y or n) ")
tet = check_str(tet) 

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
			for i in range(1): #!!!STOP program "Ctrl + C"!!!
				print( r.randint(0, 1))					
	pass	
else:
	print("Error/Ошибка")


