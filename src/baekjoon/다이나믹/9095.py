# 1 2 3더하기

d = [0]*12
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7
for i in range(4, 12):
    d[i] = (d[i-1] + d[i-2] + d[i-3])
T = int(input())
answer = []
for _ in range(T):
    n = int(input())
    answer.append(d[n])
for a in answer:
    print(a)
