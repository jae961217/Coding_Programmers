def solution(left, right):
    answer = 0

    def func(num):
        tmpnum = int(num ** 0.5)
        if num % tmpnum == 0 and num // tmpnum == tmpnum:
            return False
        return True

    for i in range(left, right + 1):
        if func(i):
            answer += i
        else:
            answer -= i

    return answer