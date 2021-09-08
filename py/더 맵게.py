import heapq

def solution(scoville, K):
    answer = 0

    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while True:
        value = heapq.heappop(heap)
        if value >= K:
            break
        if len(heap) == 0:
            answer = -1
            break
        nextvalue = heapq.heappop(heap)
        heapq.heappush(heap, value + 2 * nextvalue)
        answer += 1

    return answer