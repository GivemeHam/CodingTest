import math


def solution(n, a, b):
    idx = 1
    while True:
        idx *= 2
        a = math.ceil(a/idx) * idx
        b = math.ceil(b/idx) * idx
        if a == b:
            return int(math.log2(idx))


print(solution(16, 3, 13))
