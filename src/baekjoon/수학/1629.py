def dac(a, b):
    if b == 1:
        return a % c

    temp = dac(a, b//2)

    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp*temp*a % c


a, b, c = map(int, input().split())
result = dac(a, b)
print(result)
