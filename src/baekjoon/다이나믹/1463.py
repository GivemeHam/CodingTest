# 1로 만들기

n = int(input())

d = [0] * 1000001

d[1] = 0
d[2] = 1
d[3] = 1
for i in range(4, n+1):

    d[i] = min(d[i-1], d[i//3] if i % 3 == 0 else 9109999999,
               d[i//2]if i % 2 == 0 else 999999999)+1
print(d[n])
