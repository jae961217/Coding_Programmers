def solution(price, money, count):
    answer = -1
    count_sum = 0
    for i in range(count):
        count_sum += i + 1

    answer = count_sum * price - money
    if answer < 0:
        answer = 0
    return answer