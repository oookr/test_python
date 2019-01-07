file = "Home.html"
f = open(file)
line = f.readline()
a = 1
while line:

    if a == 1:
        print("\n--------------------Read "+ file +"--------------------\n")
    print(line, end=" ")
    line = f.readline()
    a += 1
f.close()
