import random as r
 
print ("How many numbers?")
num = int(input ())
if num > 100:
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


tet = str(input("Do you want to have fun? (y or n) "))
if tet == "n":
	print(':(')
elif  tet == "y":
	for i in range():	
		print( r.randint(0, 1))
else:
	while tet != "y":
		while tet != "n":
			
			tet = str(input("Do you want to have fun? (y or n) "))
			if tet == "n":
				print(':(')
			elif  tet == "y":
				for i in range(): #!!!STOP program "Ctrl + C"!!!	#range ()-infinitely ; range (1) - one
					print( r.randint(0, 1))
		pass	
	pass

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