def solution(routes):
    answer = 0
    cam = []
    routes.sort(key=lambda x: x[0])
    start, end = routes[0][0], routes[0][1]
    for s, e in routes:
        if s <= end:
            if e <= end:
                end = e
            start = s
        else:
            cam.append((start, end))
            start, end = s, e

    return len(cam) + 1