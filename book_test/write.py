# import os
#
# cwd = os.getcwd() # The path to the folder
# f = open("out.txt","w") # Open folder whit writing
# year = 1
# numyear = 5
# pricipal = 1000
# rate = 0.04
# print("This is (pwd)cwd: "+ cwd+" \n")
# while year <= numyear:
#     pricipal= pricipal * (1+rate)
#     print("%3d %0.2f" %(year, pricipal), file = f) # "f" is write
#     year += 1
# f.close()

import sys
sys.stdout.write("Enter your name: ")
name = sys.stdin.readline()
print("Hello, " + str(name))