info1 = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query1 = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(infos, querys):
    answer = []
    #cpp java python -
    language = [['cpp'],['java'],['python']]
    # backend frontend -
    position = [['backend'],['frontend']]
    #junior, senior, -
    nior = [['junior'],['senior']]
    #chicken, pizza -
    food = [['chicken'],['pizza']]
    #score
    score = []

    #set table
    for i, person in enumerate(infos):
      s = person.split(" ")[4]
      score.append((i,int(s)))
      for j,lan in enumerate(language):
        if lan[0] in person:
          language[j].append(i)
      for j,pos in enumerate(position):
        if pos[0] in person:
          position[j].append(i)
      for j,nio in enumerate(nior):
        if nio[0] in person:
          nior[j].append(i)
      for j,foo in enumerate(food):
        if foo[0] in person:
          food[j].append(i)
    # print(language)
    # print(position)
    # print(nior)
    # print(food)
    # print(score)

    #find with query
    for person in querys:
      #set query
      query = person.split(" and ")
      query.append(query[3].split(" ")[1])
      query[3] = query[3].split(" ")[0]
      query[4] = int(query[4])

      tempAnswer = []
      #language
      if query[0] !='-':
        for lan in language:
          if lan[0] == query[0]:
            tempAnswer.append(lan)
      #posiotion
      if query[1] !='-':
        for pos in position:
          if pos[0] == query[1]:
            tempAnswer.append(pos)
      #posiotion
      if query[2] !='-':
        for nio in nior:
          if nio[0] == query[2]:
            tempAnswer.append(nio)
      #food
      if query[3] !='-':
        for foo in food:
          if foo[0] == query[3]:
            tempAnswer.append(foo)
      # print('tempAnswer : ')
      # print(tempAnswer)
      if len(tempAnswer) == 0 :
        # print(query[4])
        # t = filter(lambda x:x[1]>=query[4], score)
        answer.append(len([x for x in score if x[1]>=query[4]]))
      #reduce
      else:
        del tempAnswer[0][0]
        answerList = tempAnswer[0]
        for temp in tempAnswer:
          if temp != ['-']:
            answerList = list(set(answerList) & set(temp))
        # print("answer : " ,answerList)
        # print(query[4])
        # print(score)
        answer.append(len([x for x in answerList if score[x][1]>=query[4]]))

    return answer

result = solution(info1, query1)
print(result)

# for person in querys:
#       #set query
#       query = person.split(" and ")
#       query.append(query[3].split(" ")[1])
#       query[3] = query[3].split(" ")[0]

#       for condition in query:
        

#       queryTable.append(query)
    