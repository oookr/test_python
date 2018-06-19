# import os
import sys 


def check_int(s):
	try:
		return int(s)#and float(x)
	except:
		print('please enter an integer!')
		sys.exit()

def check_str(x):
	try:
		return str(x) 
	except:
		print('please enter an string!')
		sys.exit()

def check_str2(x):
	try:
		# nam = (1,2,3,4,5,6,7,8,9,0)
		nam_str= ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
		# nam_all =nam + nam_str
		# return x != 0 or x != 1 or x != 2 or x != 3 or x != 4 or x != 5 or x != 6 or x != 7 or x != 8 or x != 9 or x != "0" or x != "1" or x != "2" or x != "3" or x != "4" or x != "5" or x != "6" or x != "7" or x != "8" or x != "9"
		return x != nam_str
	except:
		print('please enter an string!')
		sys.exit()

def check_num(num):
	try:
		return 1000	> num
	except:
		print ('Number >  100, enter the number < 100')
		sys.exit()
		