n = int(input())
array = []
for _ in range(n):
    array.append(input())
array = list(set(array))
array.sort()
array.sort(key=len)

for a in array:
    print(a)
