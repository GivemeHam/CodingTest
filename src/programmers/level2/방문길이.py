def solution(dirs):
    answer = 0
    CurrentPoint = [0, 0]
    array = []
    for dir in dirs:
        if dir == 'U':
            if CurrentPoint[1]+1 <= 5:
                array.append([CurrentPoint[0], CurrentPoint[1],
                              CurrentPoint[0], CurrentPoint[1]+1])
                CurrentPoint = [CurrentPoint[0], CurrentPoint[1]+1]
        if dir == 'D':
            if CurrentPoint[1]-1 >= -5:
                array.append([CurrentPoint[0], CurrentPoint[1],
                              CurrentPoint[0], CurrentPoint[1]-1])
                CurrentPoint = [CurrentPoint[0], CurrentPoint[1]-1]
        if dir == 'L':
            if CurrentPoint[0]-1 >= -5:
                array.append([CurrentPoint[0], CurrentPoint[1],
                              CurrentPoint[0]-1, CurrentPoint[1]])
                CurrentPoint = [CurrentPoint[0]-1, CurrentPoint[1]]
        if dir == 'R':
            if CurrentPoint[0]+1 <= 5:
                array.append([CurrentPoint[0], CurrentPoint[1],
                              CurrentPoint[0]+1, CurrentPoint[1]])
                CurrentPoint = [CurrentPoint[0]+1, CurrentPoint[1]]
    value = []
    for a in array:
        if a not in value and [a[2], a[3], a[0], a[1]] not in value:
            value.append(a)

    return len(value)


print(solution("ULURRDLLU"))
