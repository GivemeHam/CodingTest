from collections import deque
import copy

answer = []
n = int(input())

matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)

matrix_copy = copy.deepcopy(matrix)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
blueCnt = 0
for i in range(n):
    for j in range(n):
        if matrix_copy[i][j] != 'Z':
            cnt += 1
            if matrix_copy[i][j] == 'B':
                blueCnt += 1
            color = matrix_copy[i][j]
            queue = deque([[i, j]])
            while queue:
                q = queue.popleft()

                for k in range(4):
                    xx = q[1] + dx[k]
                    yy = q[0] + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        if matrix_copy[yy][xx] == color:
                            queue.append([yy, xx])
                            matrix_copy[yy][xx] = 'Z'
answer.append(cnt)
# RG
cnt = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] == 'G':
            cnt += 1
            color = matrix[i][j]
            queue = deque([[i, j]])
            while queue:
                q = queue.popleft()

                for k in range(4):
                    xx = q[1] + dx[k]
                    yy = q[0] + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        if matrix[yy][xx] == 'R' or matrix[yy][xx] == 'G':
                            queue.append([yy, xx])
                            matrix[yy][xx] = 'Z'
answer.append(cnt+blueCnt)
print(' '.join(map(str, answer)))
