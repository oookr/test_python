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

def check_num(num):
	try:
		return 1000	> num
	except:
		print ('Number >  100, enter the number < 100')
		sys.exit()
		