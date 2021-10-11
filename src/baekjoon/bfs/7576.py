# 토마토
from collections import deque
M, N = map(int, input().split())
queue = deque([])
weight = deque([])

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])
            weight.append(2)


def breakPoint(matrix):
    for row in matrix:
        if 0 in row:
            return False
    return True


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    cur = queue.popleft()
    w = weight.popleft()

    for i in range(4):
        xx = cur[1] + dx[i]
        yy = cur[0] + dy[i]

        if 0 <= xx < M and 0 <= yy < N and matrix[yy][xx] == 0:
            matrix[yy][xx] = w
            queue.append([yy, xx])
            weight.append(w+1)

if breakPoint(matrix):
    print(w-2)
else:
    print(-1)
