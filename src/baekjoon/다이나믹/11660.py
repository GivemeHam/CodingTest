n, m = map(int, input().split())

matrix = [[0]*(n+1)]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    matrix.append(row)
for i in range(1, n+1):
    for j in range(1, n+1):
        matrix[i][j] += matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1]

answer = []

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    sum = matrix[x2][y2] - matrix[x1-1][y2] - \
        matrix[x2][y1-1] + matrix[x1-1][y1-1]
    answer.append(sum)

for a in answer:
    print(a)
