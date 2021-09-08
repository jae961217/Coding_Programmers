from collections import deque

def solution(progresses, speeds):
    answer = []
    tmp = deque([])

    for i in range(len(progresses)):
        value, m = divmod((100 - progresses[i]), speeds[i])
        if m == 0:
            tmp.append(value)
        else:
            tmp.append(value + 1)

    while tmp:
        cnt = 1
        value = tmp[0]
        for i in range(1, len(tmp)):
            if value < tmp[i]:
                break
            cnt += 1
        answer.append(cnt)
        for i in range(cnt):
            tmp.popleft()

    return answer