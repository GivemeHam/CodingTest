def solution(clothes):
    answer = 1

    hash = {}
    for cloth, type in clothes:
        if type not in hash:
            hash[type] = 1
        else:
            hash[type] += 1

    for i in hash.values():
        answer *= i+1

    return answer-1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
