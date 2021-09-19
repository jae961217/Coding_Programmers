def solution(n):
    answer = 0

    tmp = ''

    while n:
        tmp = str(n % 3) + tmp
        n //= 3

    for i in range(len(tmp)):
        answer += int(tmp[i]) * 3 ** i

    return answer