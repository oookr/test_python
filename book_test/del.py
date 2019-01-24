import os
from sys import exit

print("List directory given by path(" + os.getcwd() + "):\n", os.listdir("."), end="\n")
file = input('The name of the file you want to delete: ')

# what show the directory
while os.listdir("."):
	print("present(" + os.getcwd() + ") directory", os.listdir("."), end="\n")
	move = input("move to" + str(os.listdir(".")) + "\n Notes:\n. - here \n.. - back\n /q - Exit\n")
	# The file name cannot contain "/"
	while "/q" in move:
		exit("Bye")
	try:
		os.listdir(move)
		print("present(" + os.getcwd() + ") directory", os.listdir(move), end="\n")
	except ValueError as error:
		print(error)

# if the file is not there:
while file not in os.listdir("."):
	print(file + " is not in this directory\n List directory: \n", os.listdir("."),
	end="\n")
	question = input("Do you want to continue, yes or no: ")
	if "n" in question[0]:
		exit("Bye")
	elif "y" in question[0]:
		file = input("The name of the file you want to delete: ")
		while file in os.listdir("."):
			os.remove(file)

# Is there a file in the directory?
while file in os.listdir("."):
	# if the file is, then the file is deleted:
	print("Deleted " + file, end=" \n")
	os.remove(file)



