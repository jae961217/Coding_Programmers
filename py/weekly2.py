def solution(scores):
    answer = ''

    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])
        value = sum(tmp)
        if (scores[i][i] == max(tmp) or scores[i][i] == min(tmp)) and tmp.count(scores[i][i]) == 1:
            value -= scores[i][i]
            value /= (len(tmp) - 1)
        else:
            value /= len(tmp)
        if value >= 90:
            answer += 'A'
        elif value >= 80:
            answer += 'B'
        elif value >= 70:
            answer += 'C'
        elif value >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer