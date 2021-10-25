def solution(triangle):
    height = len(triangle)
    for i in range(1, height):
        for j in range(len(triangle[i])):
            if j == len(triangle[i])-1:  # end
                triangle[i][j] += triangle[i-1][j-1]
            elif j == 0:  # start
                triangle[i][j] += triangle[i-1][j]
            else:  # else
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[height-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
