

def solution(name):
    answer, idx = 0, 0
    arrayInt = [min(ord('Z') - ord(x)+1, ord(x)-65) for x in name]

    print(arrayInt)

    while True:
        answer += arrayInt[idx]
        arrayInt[idx] = 0
        if sum(arrayInt) == 0:
            break

        left, right = 1, 1
        while arrayInt[idx - left] == 0:
            left += 1
        while arrayInt[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right

    return answer


print(solution('ABCDEFGHIZKLMNOPQRSTUVWXYZ'))
