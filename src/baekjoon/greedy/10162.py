n = int(input())

timer = [300, 60, 10]
answer = []

if n % 10 != 0:
    answer.append(-1)
else:
    for i in range(3):
        answer.append(n // timer[i])
        n -= (answer[i] * timer[i])

print(' '.join(map(str, answer)))
