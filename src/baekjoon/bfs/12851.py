from collections import deque
a, b = map(int, input().split())

visit = [0] * 100001

queue = deque([a])
weight = deque([0])
cnt = 0
while queue:
    q = queue.popleft()
    if q == b:
        cnt += 1

    for x in [q+1, q-1, q*2]:
        if 0 <= x < 100001 and (visit[x] == 0 or visit[q]+1 <= visit[x]):
            queue.append(x)
            visit[x] = visit[q]+1
print(visit[b])
print(cnt)
