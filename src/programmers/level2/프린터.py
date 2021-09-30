def solution(priorities, location):
    formatPrio = list(enumerate(priorities))
    i = 0
    while True:
        #get maxValue
        maxPriority = max(formatPrio, key = lambda x:x[1])
        print(formatPrio,i)
        #print
        if maxPriority[1] == formatPrio[0][1]:
          i+=1
          if location==maxPriority[0]:
            return i
          del formatPrio[0]
        else:
          temp = formatPrio[0]
          del formatPrio[0]
          formatPrio.append(temp)
result = solution([1,1,9,1,1,1], 0)
print(result)