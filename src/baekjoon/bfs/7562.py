from collections import deque


def inBoard(x, y, l):
    if 0 <= x < l and 0 <= y < l:
        return True
    else:
        return False


T = int(input())
answer = []
for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    board = [[0] * l for _ in range(l)]

    weight = deque([0])
    queue = deque([start])

    dx = [2, 2, 1, -1, -2, -2, 1, -1]
    dy = [1, -1, 2, 2, 1, -1, -2, -2]
    while queue:
        cur = queue.popleft()
        w = weight.popleft()
        if cur == end:
            answer.append(w)
            break

        for i in range(8):
            xx, yy = cur[0]+dx[i], cur[1]+dy[i]

            if inBoard(xx, yy, l):
                if board[xx][yy] == 0:
                    queue.append([xx, yy])
                    weight.append(w+1)
                    board[xx][yy] = 1
for a in answer:
    print(a)
