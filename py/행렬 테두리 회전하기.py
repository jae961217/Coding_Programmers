from collections import deque


def solution(rows, columns, queries):
    answer = []

    arr = []
    for i in range(rows):
        tmp = []
        for j in range(columns):
            tmp.append(i * columns + j + 1)
        arr.append(tmp)

    for i in queries:
        a, b, c, d = i
        value = deque([])
        for j in range(b - 1, d - 1):
            value.append(arr[a - 1][j])
        for j in range(a - 1, c - 1):
            value.append(arr[j][d - 1])
        for j in range(d - 1, b - 1, -1):
            value.append(arr[c - 1][j])
        for j in range(c - 1, a - 1, -1):
            value.append(arr[j][b - 1])
        answer.append(min(value))
        value.appendleft(value.pop())
        index = 0
        for j in range(b - 1, d - 1):
            arr[a - 1][j] = value[index]
            index += 1
        for j in range(a - 1, c - 1):
            arr[j][d - 1] = value[index]
            index += 1
        for j in range(d - 1, b - 1, -1):
            arr[c - 1][j] = value[index]
            index += 1
        for j in range(c - 1, a - 1, -1):
            arr[j][b - 1] = value[index]
            index += 1

    return answer