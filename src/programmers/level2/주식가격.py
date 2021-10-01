def solution(prices):
    answer = []
    n = len(prices)

    for i in range(n):
        x = prices[i]
        for j in range(i+1, n+1):
            if j == n:
                answer.append(j-i-1)
                break
            if x > prices[j]:
                answer.append(j-i)
                break

    return answer


print(solution([2, 3, 1, 4, 3]))
