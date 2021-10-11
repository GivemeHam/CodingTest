from collections import deque

N, M = map(int, input().split())
rel = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    rel[a-1][b-1] = 1
    rel[b-1][a-1] = 1

visits = []

for i in range(N):
    visit = [-1] * N
    queue = deque([i])
    weight = deque([0])
    visit[i] = 0
    while queue:
        cur = queue.popleft()
        w = weight.popleft()

        for j in range(N):
            if visit[j] == -1 and rel[cur][j] == 1:
                queue.append(j)
                weight.append(w+1)
                visit[j] = w+1
    visits.append(sum(visit))
print(visits.index(min(visits))+1)
# for i in range(N):
#   visit=[-1 for k in range(N)]
#   queue = deque([i])
#   weight = deque([0])
#   visit[i]=0
#   while(queue):
#     cur = queue.popleft()
#     w = weight.popleft()
#     for j in range(rel[cur]):
#       if(visit[j]==-1 and rel[cur][j]==1):
#         queue.append(j)
#         weight.append(w+1)
#         visit[j]=w+1
