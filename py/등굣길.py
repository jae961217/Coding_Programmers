def solution(m, n, puddles):
    answer = 0

    arr = [[1] * n for _ in range(m)]
    res = [[0] * n for _ in range(m)]
    for i in puddles:
        arr[i[0] - 1][i[1] - 1] = 0

    for i in range(1, n):
        if arr[0][i] != 0:
            res[0][i] = 1
        else:
            break
    for i in range(1, m):
        if arr[i][0] != 0:
            res[i][0] = 1
        else:
            break

    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            if arr[i][j] != 0:
                res[i][j] = (res[i - 1][j] + res[i][j - 1])

    print(res)

    answer = res[m - 1][n - 1] % 1000000007
    return answer