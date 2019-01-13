import os
print(" List directory given by path(" + os.getcwd() + "):\n", os.listdir("."), end="\n")

file = input('The name of the file you want to delete: ')

# Is there a file in the directory?
while file in os.listdir("."):
	# if the file is, then the file is deleted:
	try:
		os.remove(file)
	# elif the file is not there:
	except:
		qesten = input("Continue yes or no: ")
		if "n" in qesten:
			os.exit()
		elif "y" in qesten:
			file = input("The name of the file you want to delete: ")
			os.remove(file)
