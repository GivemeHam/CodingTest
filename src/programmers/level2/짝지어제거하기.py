from collections import deque


def solution(s):
    que = deque(s)
    stack = []

    while que:
        stack.append(que.popleft())
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    if stack:
        return 0
    return 1


print(solution('baabaa'))
