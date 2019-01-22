import time

def tail(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines,seartchtext):
    for line in lines:
        if seartchtext in line: yield line

wwwlog = tail(open("test.py"))
pylines = grep(wwwlog, "python")
for line in pylines:
    print(line, end=" ")
