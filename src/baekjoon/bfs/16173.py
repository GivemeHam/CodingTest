from collections import deque
n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

queue = deque([[0, 0]])
visit = []
dx = [0, 1]
dy = [1, 0]
while queue:
    q = queue.popleft()
    value = matrix[q[0]][q[1]]
    if value == -1:
        print('HaruHaru')
        exit(0)

    for i in range(2):
        xx = q[1] + dx[i] * value
        yy = q[0] + dy[i] * value

        if 0 <= xx < n and 0 <= yy < n and [yy, xx] not in visit:
            queue.append([yy, xx])
            visit.append([yy, xx])
print('Hing')
