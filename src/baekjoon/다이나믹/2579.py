# 계단오르기

N = int(input())
stair = []
maxArray = [0] * N
for _ in range(N):
    stair.append(int(input()))
maxArray[0] = stair[0]
if N > 1:
    maxArray[1] = stair[0]+stair[1]
if N > 2:
    maxArray[2] = max(stair[0], stair[1])+stair[2]
if N > 2:
    for i in range(3, N):
        maxArray[i] = max(maxArray[i-2], maxArray[i-3]+stair[i-1]) + stair[i]
    print(maxArray[-1])
else:
    print(maxArray[N-1])
