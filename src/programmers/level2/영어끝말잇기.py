import math


def solution(n, words):
    answer = []
    answer.append(words[0][0])
    idx = 0

    for i, word in enumerate(words):
        if not word in answer:
            if answer[-1][-1] != word[0]:
                # finish
                idx = i+1
                break
            answer.append(word)
        else:
            # finish
            idx = i+1
            break
    num = 0
    if idx == 0:
        return [0, 0]
    if idx % n == 0:
        num = n
    else:
        num = idx % n
    return [num, math.ceil(idx/n)]


print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
                   "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
