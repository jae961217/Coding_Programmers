def solution(n):
    answer = 0

    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b

    answer = a % 1000000007
    return answer