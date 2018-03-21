import random as r
# №1
print ("How many numbers?")
num = int(input ()) 
if num > 100: # стереть int()  поставить if int(num) > 100:
	print ("Number >  100, enter the number < 100 ")
	while num > 100 :
		if num > 100:
		#	print ("Number >  100, enter the number < 100 ")
			print ("How many numbers?")
		num = int(input ())
		if num <= 100:
			for i in range(num):	
				print( r.randint(0, 1))
	pass
elif num <= 100:
	for i in range(num):	
		print( r.randint(0, 1))
else:
	print("Error/Ошибка (report it/сообщите о ней)") 

# №2
tet = str(input("Do you want to have fun? (y or n) "))
if tet == "n":
	print(':(')
elif  tet == "y":
	while tet == "y" :
		
		for i in range(1):	
			print( r.randint(0, 1))

elif tet != "y" and tet != "n":
# else: 
	while tet != "y" and tet != "n":
		tet = str(input("Do you want to have fun? (y or n) "))
		if tet == "n":
			print(':(')
		while tet == "y":
			if  tet == "y":
				for i in range(1): #!!!STOP program "Ctrl + C"!!!
					print( r.randint(0, 1))					
	pass	
else:
	print("Error/Ошибка (report it/сообщите о ней)")		

# tet = str(input("Do you want to have fun? (y or n) "))
# if tet == "n":
# 	print(':(')
# elif  tet == "y" "":

# 	for i in range(9999999999):	
# 		print( r.randint(0, 1))
# else:
# 	while tet != "n":
# 		tet = str(input("Do you want to have fun? (y or n) "))
# 		if tet == "n":
# 			print(':(')
# 		elif  tet == "y" "":
# 			for i in range(9999999999):	
# 				print( r.randint(0, 1))
# 	while tet != "y":
# 		# pass
# 		tet = str(input("Do you want to have fun? (y or n) "))
# 		if tet == "n":
# 			print(':(')
# 		elif  tet == "y" "":
# 			for i in range(9999999999):	
# 				print( r.randint(0, 1))

	# tet = str( input( "Do you want to have fun? ( y or n) "))
	# if tet == "n":
	# 	print(':(')
	# elif  tet == "y":
	# 	for i in range(9999999999):	
	# 		print( random.randint(0, 1))
	# else:
	# 	print("oh noo!!!")