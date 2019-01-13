import os
print(" List directory given by path(" + os.getcwd() + "):\n", os.listdir("."), end="\n")

file = input("The name of the file you want to delete: ")

# Is there a file in the directory?
while os.listdir(file):
	# if the file is, then the file is deleted:
	try:
		os.remove(file)
	# elif the file is not there:
	except:
		qesten = input("Continue yes or no: ")
		if qesten in "n":
			os.exit()
		elif qesten in "y":
			file = input("The name of the file you want to delete: ")
			os.remove(file)
