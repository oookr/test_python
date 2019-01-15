def print_matches(matchtext):
    print("Поиск подстроки", matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)

matchers = [
    print_matches("python"),
    print_matches("guido"),
    print_matches("jython")
]

for m in matchers:
    m.__next__()

wwwlog = tail(open("access-log"))
for line in wwwlog:
    for m in matchers:
        m.send(line)


# import time
# def tail(f):
#     f.seek(0, 2)
#     while True:
#         line = f.readline()
#         if not line:
#             time.sleep(0.1)
#             continue
#         yield line
