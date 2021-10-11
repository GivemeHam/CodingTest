# 듣보잡

from collections import deque
N, M = map(int, input().split())

d = []
b = []
answer = []
for i in range(N):
    name = input()
    d.append(name)
for i in range(M):
    name = input()
    b.append(name)
d.sort()
b.sort()
d = deque(d)
b = deque(b)


while d and b:
    dname = d[0]
    bname = b[0]
    if dname == bname:
        answer.append(dname)
        d.popleft()
        b.popleft()

    elif dname < bname:
        d.popleft()
    else:
        b.popleft()
print(len(answer))
for a in answer:
    print(a)
