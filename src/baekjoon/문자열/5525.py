from collections import deque

n = int(input())
s = int(input())
string = input()
a = [0]
b = [0]
string += 'OOOO'
s += 4
answer = 0
for i in range(0, s-2, 2):
    if string[i] == 'I' and string[i+1] == 'O':
        if a[-1] > 0:
            a[-1] += 1
        else:
            a.append(1)
    elif string[i] == 'I':
        a.append(0)
    else:
        if a[-1] > 0:
            a[-1] -= 1
        a.append(0)
    #
    if string[i+1] == 'I' and string[i+2] == 'O':
        if b[-1] > 0:
            b[-1] += 1
        else:
            b.append(1)
    elif string[i+1] == 'I':
        b.append(0)
    else:
        if b[-1] > 0:
            b[-1] -= 1
        b.append(0)

a = set(a)
b = set(b)
print(a, b)
for aa in a:
    if aa >= n:
        answer += aa-n+1
for bb in b:
    if bb >= n:
        answer += bb-n+1

print(answer)
