# 유기농 배추
import sys
sys.setrecursionlimit(1000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(mapArray, y, x):
    mapArray[y][x] = 0

    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0 <= yy < N and 0 <= xx < M and mapArray[yy][xx] == 1:
            bfs(mapArray, yy, xx)


answer = []
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    mapArray = [[0]*M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        mapArray[b][a] = 1
    cnt = 0

    for i in range(N):
        for j in range(M):
            if mapArray[i][j] == 1:
                cnt += 1
                bfs(mapArray, i, j)
    answer.append(cnt)
for a in answer:
    print(a)
