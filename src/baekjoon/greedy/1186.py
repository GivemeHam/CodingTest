N, K = map(int, input().split())

sq = [[0] * 101 for _ in range(101)]
answer = []
count = [0] * (N+1)
maxIdx = 0
for idx in range(N):
    rect = list(map(int, input().split()))
    maxIdx = max(max(rect), maxIdx)

    for i in range(rect[0], rect[2]):
        for j in range(rect[1], rect[3]):
            sq[i][j] = idx+1
for i in range(maxIdx):
    for j in range(maxIdx):
        if sq[i][j] != 0:
            count[sq[i][j]] += 1

for _ in range(K):
    idx = count.index(max(count))
    count[idx] = -1
    answer.append(idx)
answer.sort()
for a in answer:
    print(a)
