# 섬의개수
from collections import deque

answer = []
while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = []
    cnt = 1
    for _ in range(h):
        row = list(map(int, input().split()))
        island.append(row)
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 1, 0, -1, 1, 0, -1]
    for c in range(h):
        for r in range(w):
            if island[c][r] == 1:
                cnt += 1
                queue = deque([[c, r]])
                island[c][r] = cnt
                while queue:
                    q = queue.popleft()
                    for i in range(8):
                        xx = q[1] + dx[i]
                        yy = q[0] + dy[i]

                        if 0 <= xx < w and 0 <= yy < h and island[yy][xx] == 1:
                            queue.append([yy, xx])
                            island[yy][xx] = cnt
    answer.append(cnt-1)
for a in answer:
    print(a)
