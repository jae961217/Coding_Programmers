from itertools import permutations


def solution(numbers):
    answer = 0
    res = set()

    def check(num):
        if num == '1':
            return False
        num = int(num)
        tmp = int(num ** 0.5)
        for i in range(2, tmp + 1):
            if num % i == 0:
                return False
        return True

    n = []
    for i in numbers:
        n.append(i)

    for i in range(1, len(n) + 1):
        for j in permutations(n, i):
            if j[0] == '0':
                continue
            s = ''
            for k in j:
                s += k
            if check(s):
                res.add(s)

    return len(res)