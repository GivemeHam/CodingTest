from collections import deque
# 스택 수열
n = int(input())
array = []
answer = []
for _ in range(n):
    array.append(int(input()))
que = deque(array)

stack = []
for i in range(1, n+1):
    stack.append(i)
    answer.append('+')
    while stack[-1] == que[0]:
        stack.pop()
        que.popleft()
        answer.append('-')
        if not stack:
            break
if que:
    print('NO')
else:
    for a in answer:
        print(a)
