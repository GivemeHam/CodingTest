# 미로탐색
from collections import deque

N, M = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]

visit = [[0]*M for _ in range(N)]

queue = deque([[0, 0]])
weight = deque([1])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    cur = queue.popleft()
    w = weight.popleft()

    if cur[0] == N-1 and cur[1] == M-1:
        print(w)
        break
    for i in range(4):
        xx = cur[1] + dx[i]
        yy = cur[0] + dy[i]

        if 0 <= xx < M and 0 <= yy < N and matrix[yy][xx] == '1' and visit[yy][xx] == 0:
            visit[yy][xx] = 1
            queue.append([yy, xx])
            weight.append(w+1)
