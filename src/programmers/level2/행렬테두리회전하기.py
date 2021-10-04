def solution(rows, columns, queries):
    answer = []
    board = [[y*columns+x+1 for x in range(columns)] for y in range(rows)]

    for query in queries:
        y1, x1, y2, x2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        point1, point2 = board[y1][x1], board[y2][x2]

        # 가로 최소
        minValue = min(board[y1][x1:x2+1] + board[y2][x1:x2+1])

        # 좌
        for i in range(y1, y2):
            board[i][x1] = board[i+1][x1]
            minValue = min(board[i][x1], minValue)
        # 우
        for i in range(y2, y1, -1):
            board[i][x2] = board[i-1][x2]
            minValue = min(board[i][x2], minValue)
        # 위
        board[y1][x1+1:x2+1] = board[y1][x1:x2]
        board[y1][x1+1] = point1
        # 아래
        board[y2][x1:x2] = board[y2][x1+1:x2+1]
        board[y2][x2-1] = point2

        answer.append(minValue)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
