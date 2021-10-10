# 게임
import math

# 게임횟수, 이긴게임
X, Y = map(int, input().split())
Z = int((Y*100/X))

# binarySearch
left, right = 1, 1000000000
while left < right:
    mid = (left + right)//2
    m = int(((Y+mid)*100/(X+mid)))
    if Z >= m:
        left = mid + 1
    else:
        right = mid
print(right if int(((Y+right)*100/(X+right))) > Z else -1)
