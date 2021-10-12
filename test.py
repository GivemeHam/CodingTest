
def D(n):
    return n*2 if n*2 <= 9999 else (n*2) % 10000


print(D(1111111))
