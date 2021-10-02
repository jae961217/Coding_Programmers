from functools import cmp_to_key

def solution(numbers):
    answer = ''

    def cmp(x, y):
        x, y = str(x), str(y)
        tmp1 = x + y
        tmp2 = y + x
        if tmp1 > tmp2:
            return -1
        elif tmp2 > tmp1:
            return 1
        else:
            return 0

    numbers = sorted(numbers, key=cmp_to_key(cmp))

    for i in numbers:
        answer += str(i)
    if answer[0] == '0':
        answer = '0'
    return answer