import heapq

def solution(jobs):
    count = len(jobs)
    answer = 0
    time = 0
    heap = []
    jobs.sort()

    while jobs:
        for i in jobs:
            if time >= i[0]:
                heapq.heappush(heap, [i[1], i[0]])
            else:
                break
        if heap:
            tmp = heapq.heappop(heap)
            time += tmp[0]
            answer += (time - tmp[1])
            jobs.remove([tmp[1], tmp[0]])
            heap = []
        else:
            time = jobs[0][0] + jobs[0][1]
            answer += jobs[0][1]
            del jobs[0]
    answer //= count
    return answer