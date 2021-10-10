def queen(graph, r, n):
    count = 0

    if r == n:
        print(graph)
        return 1
    for j in range(n):
        graph[r] = j
        for i in range(r):
            if abs(graph[i]-graph[r]) == abs(r-i) or graph[i] == graph[r]:
                break
        else:
            count += queen(graph, r+1, n)

    return count


def solution(n):

    return queen([0]*n, 0, n)


print(solution(4))
