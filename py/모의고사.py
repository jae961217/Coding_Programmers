def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    onecnt, twocnt, thrcnt = 0, 0, 0

    for iIndex, i in enumerate(answers):
        if i == one[iIndex % len(one)]: onecnt += 1
        if i == two[iIndex % len(two)]: twocnt += 1
        if i == thr[iIndex % len(thr)]: thrcnt += 1

    value = max(onecnt, twocnt, thrcnt)
    if value == onecnt: answer.append(1)
    if value == twocnt: answer.append(2)
    if value == thrcnt: answer.append(3)

    return answer