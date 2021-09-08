def solution(word):
    answer = 0
    res = []

    def func(s):
        if len(s) > 4:
            return
        for i in "AEIOU":
            res.append(s + i)
            func(s + i)

    func("")
    res.sort()
    answer = res.index(word) + 1

    return answer