def solution(clothes):
    answer = 0
    tmp = dict()
    for i in clothes:
        if i[1] in tmp:
            tmp[i[1]].append(i[0])
        else:
            tmp[i[1]] = [i[0]]

    for i in tmp:
        if answer == 0:
            answer += (len(tmp[i]) + 1)
        else:
            answer *= (len(tmp[i]) + 1)

    return answer - 1