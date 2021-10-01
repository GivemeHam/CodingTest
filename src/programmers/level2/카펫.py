def solution(brown, yellow):
    answer = []
    h = 0
    while True:
        if h > yellow:
            print('?')
            break
        h += 1

        if yellow % h == 0:
            w = yellow // h
            print('h : ', h, 'w : ', w)

            if brown == 2*(w+2) + 2*(h+2) - 4:
                return [w+2, h+2]

    return answer


print(solution(10, 2))
