def solution(citations):
    citations.sort()
    size = len(citations)
    for i in range(size):
        if citations[i] >= size - i:
            return size - i

    return 0