# dfs & bfs
from collections import deque
n, m, start = map(int, input().split())
matrix = [[0]*n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1], matrix[b-1][a-1] = 1, 1

# bfs
queue = deque([start-1])
visit = [0] * n
answer_bfs = []
while queue:
    q = queue.popleft()
    visit[q] = 1
    answer_bfs.append(q+1)
    for i in range(n):
        if matrix[q][i] == 1 and visit[i] == 0:
            queue.append(i)
            visit[i] = 1
# dfs
stack = [start-1]
visit = [0] * n
answer_dfs = []


def dfs(s):
    global answer_dfs, visit, matrix
    visit[s] = 1
    answer_dfs.append(s+1)
    for i in range(n):
        if matrix[s][i] == 1 and visit[i] == 0:
            dfs(i)


dfs(start-1)
answer_bfs = map(str, answer_bfs)
answer_dfs = map(str, answer_dfs)
print(' '.join(answer_dfs))
print(' '.join(answer_bfs))
