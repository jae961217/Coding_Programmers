def solution(a, b):
    answer = ''

    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(a - 1):
        total += month[i]
    total += b - 1
    tmp1, tmp2 = divmod(total, 7)
    if tmp2 == 0:
        answer = "FRI"
    elif tmp2 == 1:
        answer = "SAT"
    elif tmp2 == 2:
        answer = "SUN"
    elif tmp2 == 3:
        answer = "MON"
    elif tmp2 == 4:
        answer = "TUE"
    elif tmp2 == 5:
        answer = "WED"
    elif tmp2 == 6:
        answer = "THU"

    return answer