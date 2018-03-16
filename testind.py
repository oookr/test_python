import random

# print us p 
num_1 = float(input ("Entet first num: "))
num_2 = float(input ("Entet second num: "))
res1 = float(num_1 + num_2)
print ("Result is one", res1)
res2 = float(num_1 + num_2 + res1)
print ("Result is two", res2)
res = float(res1 + res2)
print ("Sum of results", res) 
num_3 = int(input ("Entet  third num: "))
for i in range (num_3):
	print( random.randint(0, 1))