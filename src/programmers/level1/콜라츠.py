def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            break
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3+1
    if i == 499:
        return -1
    else:
        return i


result = solution(6)

for i in range(3):
    print(i)
