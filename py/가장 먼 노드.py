from collections import deque


def solution(n, edge):
    arr = [[] for _ in range(n + 1)]
    res = [-1] * (n + 1)
    res[1] = 0

    def func():
        dq = deque()
        dq.append(1)

        while dq:
            value = dq.popleft()
            for i in arr[value]:
                if res[i] == -1:
                    res[i] = res[value] + 1
                    dq.append(i)

    for i, j in edge:
        arr[i].append(j)
        arr[j].append(i)
    func()
    return res.count(max(res))