import math


def solution(n, k):
    answer = []
    tmp = [i for i in range(1, n + 1)]
    while n:
        fact = math.factorial(n - 1)
        index = k // fact
        k = k % fact
        if k:
            answer.append(tmp.pop(index))
        else:
            answer.append(tmp.pop(index - 1))
        n -= 1

    return answer