from collections import deque


def solution(priorities, location):
    answer = 0

    dq = deque([])

    for iIndex, i in enumerate(priorities):
        dq.append([i, iIndex])

    while True:
        tmp = dq.popleft()
        answer += 1
        if len(dq) == 0:
            break
        value = max(dq)
        if value[0] > tmp[0]:
            answer -= 1
            dq.append(tmp)
        elif tmp[1] == location:
            break

    return answer