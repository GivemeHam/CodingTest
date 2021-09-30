def change(s,n):
  temp = ord(s)
  if 65<=temp<=90:
    if temp+n >90:
      return chr(temp+n-26)
    else:
      return chr(temp+n)
  elif 97<=temp<=122:
    if temp+n >122:
      return chr(temp+n-26)
    else:
      return chr(temp+n)
  return ' '

def solution(s, n):
    answer = ''
    for w in s:
      answer += change(w,n)
    return answer

result = solution("Z", 25)
print(result)
