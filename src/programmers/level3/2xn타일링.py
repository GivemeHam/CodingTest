def solution(n):
    answer = 0
    a1 = 1
    a2 = 1
    a3 = 0
    for i in range(n):
        a3 = a1+a2
        a1 = a2 % 1000000007
        a2 = a3 % 1000000007

    return a1


print(solution(7))
