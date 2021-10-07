def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = ''
        for s in skill_tree:
            if s in skill:
                skill_list += str(skill.index(s))
        flag = 0
        for k in skill_list:
            if k != str(skill_list.index(k)):
                flag = 1
                break
        if flag == 0:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
