# 토마토
from collections import deque
M, N, Z = map(int, input().split())
queue = deque([])
weight = deque([])

matrix = []
for k in range(Z):
    matrix2 = []
    for i in range(N):
        matrix2.append(list(map(int, input().split())))
        for j in range(M):
            if matrix2[i][j] == 1:
                queue.append([k, i, j])
                weight.append(2)
    matrix.append(matrix2)


def breakPoint(matrix):
    for h in matrix:
        for row in h:
            if 0 in row:
                return False
    return True


dz = [0, 0, 0, 0, 1, -1]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
while queue:
    cur = queue.popleft()
    w = weight.popleft()

    for i in range(6):
        xx = cur[2] + dx[i]
        yy = cur[1] + dy[i]
        zz = cur[0] + dz[i]

        if 0 <= xx < M and 0 <= yy < N and 0 <= zz < Z and matrix[zz][yy][xx] == 0:
            matrix[zz][yy][xx] = w
            queue.append([zz, yy, xx])
            weight.append(w+1)


if breakPoint(matrix):
    print(w-2)
else:
    print(-1)
