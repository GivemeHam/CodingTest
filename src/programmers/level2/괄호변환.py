def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack


def divide(w):
    openP = 0
    closeP = 0

    for i in range(len(w)):
        if w[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return w[:i + 1], w[i + 1:]


def s(p):
    # 1
    if p == "":
        return ""
    # 2
    u, v = divide(p)
    print('{} - {}'.format(u, v))
    # 3
    if is_correct(u):
        return u + s(v)
    else:  # 4
        return

    return ''


def solution(p):
    return s(p)


result = solution(")()))((()")
print(result)
