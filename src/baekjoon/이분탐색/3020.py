# 개똥벌레

l, h = map(int, input().split())
idx = 0
array = [0]*h
for _ in range(l):
    idx += 1
    a = int(input())

    if idx % 2 == 1:
        for i in range(h-a, h):
            array[i] += 1
    else:
        for i in range(a):
            array[i] += 1
minValue = min(array)
print(minValue, array.count(minValue))
