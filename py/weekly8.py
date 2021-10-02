def solution(sizes):
    answer = 0
    a, b = 0, 0
    for i in sizes:
        tmp = i
        tmp.sort()
        if tmp[0] > a:
            a = tmp[0]
        if tmp[1] > b:
            b = tmp[1]

    return a * b