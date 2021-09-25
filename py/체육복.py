def solution(n, lost, reserve):
    setlost = set(lost) - set(reserve)
    setreserve = set(reserve) - set(lost)

    for i in setreserve:
        if i - 1 in setlost:
            setlost.remove(i - 1)
        elif i + 1 in setlost:
            setlost.remove(i + 1)

    return n - len(setlost)