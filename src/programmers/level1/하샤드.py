def solution(x):
    answer = True
    x1 = x
    sum = 0
    while(True):
      sum+= x1 % 10
      x1 = x1//10
      if x1<1:
        break
    if x%sum!=0: answer = False
    return answer

result = solution(12)
print(result)