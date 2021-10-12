# 동전
from collections import deque
n, k = map(int, input().split())

coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)
queue = deque(coins)

coinN = 0

while queue:
    if k == 0:
        break
    q = queue.popleft()
    if k >= q:
        coinN += k//q
        k = k % q
print(coinN)
