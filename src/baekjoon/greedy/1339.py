# 단어수학

array = []
arrayTemp = []
check = ['-' for x in range(10)]
idx = 8
answer = 0
# input
n = int(input())
for _ in range(n):
    a = input()
    array.append(a)
arrayTemp = array[:]
# set Number
while True:
    array.sort(key=len, reverse=True)
    if len(array[0]) == 0:
        break
    if check[idx] == '-' and check.count(array[0][0]) == 0:
        check[idx] = array[0][0]
        array[0] = array[0][1:]
        idx -= 1
    elif check.count(array[0][0]) != 0:
        array[0] = array[0][1:]

# change
for word in arrayTemp:
    num = ''.join([str(check.index(a)) for a in word])
    answer += int(num)
print(answer)
