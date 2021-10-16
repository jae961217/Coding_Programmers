from collections import deque


def solution(maps):
    answer = 0

    dist = [[-1] * len(maps[0]) for _ in range(len(maps))]
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    dq = deque([])
    dq.append([0, 0])
    visited[0][0] = 1
    dist[0][0] = 1

    while dq:
        ty, tx = dq.popleft()

        for y, x in move:
            if 0 <= y + ty < len(maps) and 0 <= x + tx < len(maps) and visited[y + ty][x + tx] == 0 and maps[y + ty][
                x + tx] == 1:
                if dist[y + ty][x + tx] > dist[ty][tx] + 1 or dist[ty + y][tx + x] == -1:
                    dq.append([y + ty, x + tx])
                    visited[y + ty][x + tx] = 1
                    dist[y + ty][x + tx] = dist[ty][tx] + 1

    return dist[-1][-1]