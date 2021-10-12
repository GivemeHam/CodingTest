# 피보나치
answer = []
T = int(input())
d = [[0, 0]] * 41

d[0] = [1, 0]
d[1] = [0, 1]
for i in range(2, 41):
    d[i] = [d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1]]
for _ in range(T):
    n = int(input())
    answer.append(d[n])
for a in answer:
    print(a[0], a[1])
