from collections import deque

def solution(n, computers):
    answer = 0

    arr = [[0] * n for _ in range(n)]
    check = [False] * n
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1: arr[i][j] = 1

    for i in range(n):
        if check[i] == False:
            answer += 1
            dq = deque([i])
            while dq:
                tmp = dq.popleft()
                check[tmp] = True
                for i in range(n):
                    if arr[tmp][i] == 1 and check[i] == 0:
                        dq.append(i)

    return answer