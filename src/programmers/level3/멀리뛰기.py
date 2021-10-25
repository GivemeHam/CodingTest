def solution(n):
    answer = 0
    a1 = 1
    a2 = 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(n-1):
        a2, a1 = (a1 + a2) % 1234567, a2 % 1234567

    return a1
