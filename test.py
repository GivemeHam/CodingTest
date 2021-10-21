from collections import deque


def solution(macaron):
    matrix = [[0]*6 for _ in range(6)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for m in macaron:
        for j in range(5, 0, -1):
            if matrix[j][m[0]-1] != 0:
                matrix[j][m[0]-1] = m[1]  # 떨어짐

            # BFS로 부수기
            for a in range(6):
                for b in range(6):
                    if matrix[a][b] != 0:
                        color = matrix[a][b]
                        queue = deque([[a, b]])
                        weight = deque(1)
                        record = []
                        while queue:
                            q = queue.popleft()
                            w = weight.popleft()

                            for i in range(4):
                                yy = q[0]+dy[i]
                                xx = q[1]+dx[i]
                                if matrix[yy][xx] == color:
                                    queue.append([yy, xx])
                                    record.append([yy, xx])
                                    weight.append(w+1)
                        if w >= 4:
                            for r in record:
                                matrix[r[0]][r[1]] = 0

                # 부숴진거 아래로 내리기
                for a in range(6):
                    for b in range(, 0, -1):
                        matrix[b][a]

    return matrix


print(solution([[1, 1], [2, 1], [1, 2], [3, 3], [
      6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]	))


# def solution(leave, day, holidays):
#     days = ['SUN', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON']
#     calendar = [0] * 31
#     maxHolidays = -1
#     firstSaturday = days.index(day) if days.index(day) != 0 else 7
#     firstSunday = firstSaturday+1 if firstSaturday != 7 else 1

#     for i in range(5):
#         sat = firstSaturday + (i*7)
#         sun = firstSunday + (i*7)
#         if sat not in holidays and sat <= 30:
#             holidays.append(sat)

#         if sun not in holidays and sun <= 30:
#             holidays.append(sun)
#     for i in range(len(holidays)):
#         calendar[holidays[i]] = 1
#     # holidays.sort()
#     # print(holidays)

#     for i in range(1, 31):
#         holi = 0
#         l = leave
#         for j in range(i, 31):
#             if calendar[j] == 0:  # 평일
#                 l -= 1
#                 if l == -1:  # 평일 + 휴무 X
#                     break
#             holi += 1
#         if holi > maxHolidays:
#             # print(holi, i)
#             maxHolidays = holi

#     return maxHolidays


# print(solution(3, 'SUN', [2, 6, 17, 29]	))
print(solution(4, 'FRI', [6, 21, 23, 27, 28]	))


# def solution(registered_list, new_id):
#     flag = 0
#     numIdx = len(new_id)
#     alph = 0
#     num = 0
#     for i in range(len(new_id)):
#         if ord('a') <= ord(new_id[i]) <= ord('z'):
#             alph += 1
#         elif ord('0') <= ord(new_id[i]) <= ord('9') and flag == 0:
#             flag = 1
#             num += 1
#             numIdx = i
#         else:
#             num += 1

#     number = 1
#     alpha = new_id[0:numIdx]

#     if numIdx != len(new_id):  # num 존재
#         number = int(new_id[numIdx:])

#     if new_id not in registered_list:  # 아이디 존재 x
#         return new_id
#     else:
#         idx = number
#         while True:
#             newId = alpha+str(idx)
#             if newId not in registered_list:
#                 return newId
#             idx += 1


# print(solution(	["cow", "cow1", "cow2", "cow3", "cow4",
#                  "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
