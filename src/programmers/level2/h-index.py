def solution(citations):
    answer = 0
    for i in range(len(citations), 0, -1):
        filterArray = [x for x in citations if x >= i]
        if len(filterArray) >= i:
            return i
    return answer


print(solution([0, 1, 2]))
