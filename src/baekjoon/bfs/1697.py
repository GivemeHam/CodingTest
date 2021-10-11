# 숨바꼭질
from collections import deque

start, end = map(int, input().split())

queue = deque([start])
weight = deque([0])
visit = []
while queue:
    cur = queue.popleft()
    w = weight.popleft()
    dx = [cur-1, cur+1, cur*2]

    if cur == end:
        print(w)
        break

    for x in dx:
        if x >= 0 and x not in visit and x <= 100000:
            queue.append(x)
            weight.append(w+1)
            visit.append(x)
