# 보석 도둑
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
items = []
for _ in range(N):
    heapq.heappush(items, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    heapq.heappush(bags, int(sys.stdin.readline()))

answer = 0

print(bags)
print(items)

tempBags = []
while bags:
    bag = heapq.heappop(bags)

    while items and items[0][0] <= bag:
        [w, m] = heapq.heappop(items)
        heapq.heappush(tempBags, -m)
    if tempBags:
        answer -= heapq.heappop(tempBags)
print(answer)
