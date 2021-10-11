N, M = map(int, input().split())
rel = [[0]*N for _ in range(N)]


def bfs(rel, start, end, cnt):
    minValue = 10000000
    if rel[start][end] == 1:
        return cnt+1
    else:
        for i in range(N):
            if rel[start][i] == 1:
                rel[start][i] = 0
                rel[i][start] = 0
                cnt = bfs(rel, i, end, cnt+1)
                minValue = min(minValue, cnt)
                rel[start][i] = 1
                rel[i][start] = 1
    return min(minValue, cnt+1)


for _ in range(M):
    a, b = map(int, input().split())
    rel[a-1][b-1] = 1
    rel[b-1][a-1] = 1
minValue = 100000000
cbArray = []
for i in range(N):
    cb = 0
    for j in range(N):
        if i != j:
            cb += bfs(rel, i, j, 0)
            if cb > 1000:
                print(i, j)
    cbArray.append(cb)
print(cbArray.index(min(cbArray))+1)
