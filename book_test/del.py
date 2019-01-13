import os
from sys import exit

print(" List directory given by path(" + os.getcwd() + "):\n", os.listdir("."), end="\n")
file = input('The name of the file you want to delete: ')

# Is there a file in the directory?
while file in os.listdir("."):
	# if the file is, then the file is deleted:
	try:
		os.remove(file)
	# elif the file is not there:
	except ValueError:
		question = input("Continue yes or no: ")
		if "n" in question:
			exit()
		elif "y" in question:
			file = input("The name of the file you want to delete: ")
			os.remove(file)
