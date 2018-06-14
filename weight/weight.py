# import sys
# import os
# import math

growth = input ("Enter the growth: ")
growth = float(growth)
resg =  (growth - 100) * 0.9
print(resg)
weight = input("Enter your weight: ")
resg= float(resg); weight = float(weight)
end = resg - weight 
print ("#1 End =", end)
# end *= -1
if end >= 2.5:
	print ("You should have podnabrat weight",  end)
elif end <= -2.5:
	print("You should've lost weight on ", end )
else:
	print("Your weight is normal if you are fifty years old fat.")
print ("#2 End =", end)