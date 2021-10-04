answer = [0]
globalN = 0
globalK = 0


def find(roadMap, place, s, memory):
    global answer, N, K
    for i in range(1, globalN):
        if roadMap[place][i] != 10001 and memory.count(i) == 0:
            if s+roadMap[place][i] <= globalK:

                answer.append(i)
                memory.append(i)
                find(roadMap, i, s+roadMap[place][i], memory)
                memory.pop()

    return


def solution(N, road, K):
    roadMap = [[10001 for col in range(N)] for row in range(N)]
    global answer, globalN, globalK
    globalN = N
    globalK = K

    for r in range(len(road)):
        if roadMap[road[r][0]-1][road[r][1]-1] > road[r][2]:
            roadMap[road[r][0]-1][road[r][1]-1] = road[r][2]
            roadMap[road[r][1]-1][road[r][0]-1] = road[r][2]
    temp = find(roadMap, 0, 0, [0])
    answer = set(answer)
    return len(answer)


print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
      3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
