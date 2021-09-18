def solution(lottos, win_nums):
    answer = []
    zero, cnt = 0, 0

    for i in lottos:
        if i == 0:
            zero += 1
        elif i in win_nums:
            cnt += 1

    answer.append(7 - cnt - zero)
    answer.append(7 - cnt)

    if cnt == 0:
        answer[1] -= 1
        if zero == 0:
            answer[0] -= 1

    return answer