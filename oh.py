# import sys 

# from import_my import check_str
from import_my import check_int
from import_my import check_num
n_ch = input ()
n_int = check_int(n_ch)
# n_num = check_num(n_int)
# n = n_num
n = n_int
xq = 0
aq = 1

if n < 1000 and n > 0:
	print ("Your result:")
	for op in range(n):
		xq += aq
		print ("l#",xq)
	pass
elif n > 1000 or n <= 0:
	print ("Number > 1000 or number < 0, enter the number < 1000 and number > 0!")
