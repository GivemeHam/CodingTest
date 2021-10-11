from collections import deque
T = int(input())
answer = []
for _ in range(T):
    n, idx = map(int, input().split())
    prin = list(map(int, input().split()))

    que = deque(prin)
    queIdx = deque([x for x in range(n)])
    i = 0
    while que:
        maxValue = max(que)
        while que[0] != maxValue:
            que.append(que.popleft())
            queIdx.append(queIdx.popleft())
        else:
            que.popleft()
            temp = queIdx.popleft()
            i += 1
            if temp == idx:
                answer.append(i)
for a in answer:
    print(a)
