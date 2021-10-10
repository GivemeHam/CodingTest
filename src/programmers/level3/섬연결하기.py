minValue = 10000


def dfs(array, start, end, cnt, road):
    global minValue
    road.append(start)

    for idx, cost in enumerate(array[start]):
        if idx in road:
            continue
        if idx == end:
            minValue = min(cnt+cost, minValue)
            return
        dfs(array, idx, end, cnt+cost, road)


def solution(n, costs):
    global minValue
    answer = [-1]*n
    array = [[0] * n for _ in range(n)]
    for cost in costs:
        array[cost[0]][cost[1]] = cost[2]
        array[cost[1]][cost[0]] = cost[2]
    for a in array:
        print(a)

    minValue = 10000
    dfs(array, 0, 3, 0, [])
    print(minValue)

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
