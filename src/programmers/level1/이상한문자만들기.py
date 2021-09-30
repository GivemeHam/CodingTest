def solution(s):
    answer = ''
    sentense = s.split(' ')

    for word in sentense:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '

    return answer[]


result = solution('     try hello world')
print(result)
