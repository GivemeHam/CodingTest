def solution(n):
    answer = 0
    for k in range(2,n+1):
        flag=0
        for i in range(2,int(k**(0.5))+1):
          if k%i==0:
            flag=1
            break
        if flag ==0:
            answer+=1
    return answer

result = solution(10)
print(result)