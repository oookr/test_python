import os
from sys import exit

print("List directory given by path(" + os.getcwd() + "):\n", os.listdir("."), end="\n")
file = input('The name of the file you want to delete: ')

# Is there a file in the directory?
while file in os.listdir("."):
	# if the file is, then the file is deleted:
	os.remove(file)

# elif the file is not there:
while file not in os.listdir("."):
	print(file + " is not in this directory\n List directory \n", os.listdir("."),
	end="\n")
	question = input("Do you want to continue, yes or no: ")
	while "n" in question[0]:
		exit("Bye")
	if "y" in question[0]:
		file = input("The name of the file you want to delete: ")
		while file in os.listdir("."):
			file = input("The name of the file you want to delete: ")
			os.remove(file)

