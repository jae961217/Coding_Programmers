def solution(table, languages, preference):
    arr = [i.split() for i in table]
    res = dict()
    for i in arr:
        res[i[0]] = 0

    for iIndex, i in enumerate(languages):
        for j in arr:
            if i in j:
                res[j[0]] += preference[iIndex] * (6 - j.index(i))
    res = sorted(res.items(), key=lambda x: (-x[1], x[0]))

    return res[0][0]