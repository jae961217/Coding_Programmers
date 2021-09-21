from itertools import combinations as c


def solution(orders, course):
    answer = []

    res = []
    value = []
    for cnt in course:
        setmenu = dict()
        for order in orders:
            order = sorted(order)
            for i in c(order, cnt):
                tmp = "".join(i)
                if tmp in setmenu:
                    setmenu[tmp] += 1
                else:
                    setmenu[tmp] = 1
        res.append(sorted(setmenu.items(), key=lambda x: x[1], reverse=True))

    for i in res:
        if len(i) == 0 or i[0][1] == 1:
            continue
        value = i[0][1]
        for j in i:
            if j[1] < value:
                break
            answer.append(j[0])

    return sorted(answer)