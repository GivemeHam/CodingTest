n = int(input())

answer = 0

for i in range(1, n+1):
    idx = 1
    while (5**idx) <= i:
        if i % (5**idx) == 0 and i % (5**(idx+1)) != 0:
            answer += idx
            break
        idx += 1
print(answer)
