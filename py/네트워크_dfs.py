def solution(n, computers):
    answer = 0

    def func(num):
        check[num] = True
        for i in range(n):
            if arr[num][i] == 1 and check[i] == 0:
                func(i)

    arr = [[0] * n for _ in range(n)]
    check = [False] * n
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1: arr[i][j] = 1

    for i in range(n):
        if check[i] == False:
            func(i)
            answer += 1

    return answer