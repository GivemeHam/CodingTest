width = 0
height = 0
minValue = 10000000
globalMaps = []


def bfs(y, x, s):
    global minValue, width, height
    # for g in globalMaps:
    #     print(g)
    # print('--------------')
    if y >= height or y < 0 or x >= width or x < 0:
        return
    if globalMaps[y][x] != 1:
        return
    globalMaps[y][x] = s

    if y == height-1 and x == width-1:
        if minValue > s:
            minValue = s
            globalMaps[y][x] = 1
            return

    bfs(y+1, x, s+1)
    bfs(y-1, x, s+1)
    bfs(y, x+1, s+1)
    bfs(y, x-1, s+1)
    globalMaps[y][x] = 1


def solution(maps):
    global width, height, globalMaps, minValue
    minValue = 2100000000
    globalMaps = maps[:]

    width = len(maps[0])
    height = len(maps)

    bfs(0, 0, 2)
    if minValue == 10000000:
        return -1
    return minValue-1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
