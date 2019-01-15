def print_matches(matchtext):
    print("Поиск подстроки", matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)
