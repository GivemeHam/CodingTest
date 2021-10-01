from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    que = deque(people)

    while len(que) > 1:
        if que[-1] > limit:
            que.pop()
        elif que[-1] + que[0] <= limit:
            que.pop()
            que.popleft()
        else:
            que.pop()
        answer += 1
    if que:
        answer += 1

    return answer
