from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    w = 0
    while bridge:
        answer += 1
        w -= bridge.popleft()
        if truck_weights:
            if w + truck_weights[0] <= weight:
                tmp = truck_weights.pop(0)
                bridge.append(tmp)
                w += tmp
            else:
                bridge.append(0)

    return answer