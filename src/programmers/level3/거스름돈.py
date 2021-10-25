

def solution(n, money):
    array = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            array[i] += array[i-m]

    return array[n] % 1000000007
