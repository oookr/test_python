import subprocess
import sys
# input("")for as.png

a=1
while a < 3: 	
	touch= r'start D:\git\git-bash.exe touch asa.txt'
	rm = r'start D:\git\git-bash.exe rm asa.txt'
	subprocess.Popen(touch,shell = True)
	subprocess.Popen(rm,shell = True)
	a = a + 1
	print()
	print("if")
	if a >= 10:
		print("if a >= 10")
		sys.exit()
if a >= 10:
	print("elif")
	sys.exit()
else:
	print ("else")
	sys.exit()