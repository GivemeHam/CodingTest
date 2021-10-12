from collections import deque
n = int(input())


def D(n):
    return n*2 if n*2 <= 9999 else (n*2) % 10000


def S(n):
    return n-1 if n-1 >= 0 else 9999


def L(n):
    string = str(n).rjust(4, '0')
    return int(string[1:4] + string[0])


def R(n):
    string = str(n).rjust(4, '0')
    return int(string[3] + string[0:3])


answer = []
for _ in range(n):
    a, b = map(int, input().split())

    queue = deque([a])
    weight = deque([''])
    visit = [0]*10000
    visit[a] = 1
    while queue:
        q = queue.popleft()
        w = weight.popleft()
        if q == b:
            answer.append(w)
            break

        value = D(q)
        if visit[value] == 0:
            queue.append(value)
            weight.append(w + 'D')
            visit[value] = 1

        value = S(q)
        if visit[value] == 0:
            queue.append(value)
            weight.append(w + 'S')
            visit[value] = 1

        value = L(q)
        if visit[value] == 0:
            queue.append(value)
            weight.append(w + 'L')
            visit[value] = 1

        value = R(q)
        if visit[value] == 0:
            queue.append(value)
            weight.append(w + 'R')
            visit[value] = 1
for a in answer:
    print(a)
