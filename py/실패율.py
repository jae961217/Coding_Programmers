def solution(N, stages):
    answer = []
    size = len(stages)

    tmp = dict()
    res = dict()
    for i in stages:
        if i > N:
            continue
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    tmp = sorted(tmp.items())

    for i in tmp:
        res[i[0]] = i[1] / size
        size -= i[1]

    res = sorted(res.items(), key=lambda x: x[1], reverse=True)

    for i in res:
        answer.append(i[0])

    for i in range(1, N + 1):
        if not i in answer:
            answer.append(i)

    return answer