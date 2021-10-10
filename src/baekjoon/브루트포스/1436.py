n = int(input())
i, idx = 666, 0
while True:
    strI = str(i)
    if '666' in strI:
        idx += 1
        if idx == n:
            print(strI)
            break
    i += 1
