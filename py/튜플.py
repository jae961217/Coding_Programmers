def solution(s):
    answer = []

    value = dict()

    s = s[2:-2].split("},{")

    for i in s:
        tmp = i.split(',')
        for j in tmp:
            if j in value:
                value[j] += 1
            else:
                value[j] = 1

    value = sorted(value.items(), key=lambda x: x[1], reverse=True)
    for i in value:
        answer.append(int(i[0]))

    return answer