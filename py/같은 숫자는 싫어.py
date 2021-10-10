def solution(arr):
    answer = []
    check = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == check:
            arr[i] = -1
        else:
            check = arr[i]

    for i in arr:
        if i != -1:
            answer.append(i)

    return answer