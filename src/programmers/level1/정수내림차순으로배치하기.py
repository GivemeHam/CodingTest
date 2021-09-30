def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    temp = "".join(answer)
    
    return temp

result = solution(118372)
print(result)