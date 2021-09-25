def solution(s):
    answer = 0

    tmp = []
    for i in s:
        if len(tmp) > 0:
            if tmp[-1] == i:
                tmp.pop()
            else:
                tmp.append(i)
        else:
            tmp.append(i)

    if len(tmp) == 0:
        answer = 1

    return answer