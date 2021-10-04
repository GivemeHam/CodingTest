def solution(N, road, K):
    roadMap = [[5000000000 for col in range(N)] for row in range(N)]
    answer = 0

    for r in range(len(road)):
        if roadMap[road[r][0]-1][road[r][1]-1] > road[r][2]:
            roadMap[road[r][0]-1][road[r][1]-1] = road[r][2]
            roadMap[road[r][1]-1][road[r][0]-1] = road[r][2]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if roadMap[i][k] + roadMap[k][j] < roadMap[i][j]:
                    roadMap[i][j] = roadMap[i][k] + roadMap[k][j]

    roadMap[0][0] = 0
    answer = len([x for x in roadMap[0] if x <= K])

    return answer


print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
      3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
