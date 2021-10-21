from collections import deque
import heapq
N, M = map(int, input().split())
answer = []
heap = []
indegree = [0] * (N+1)
matrix = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    indegree[b] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)
while heap:
    point = heapq.heappop(heap)
    answer.append(point)
    for p in matrix[point]:
        indegree[p] -= 1
        if indegree[p] == 0:
            heapq.heappush(heap, p)
answer = ' '.join(map(str, answer))
print(answer)
