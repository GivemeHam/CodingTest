def solution(n):
    temp = format(n,'b')
    num1 = str(temp).count('1')
    i = n
    while True:
        i+=1
        temp = format(i,'b')
        num2 = str(temp).count('1')
        if num1 == num2:
          return i
      

rst = solution(78)
print(rst)