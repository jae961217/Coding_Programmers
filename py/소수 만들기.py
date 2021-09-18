from itertools import combinations

def check(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def solution(nums):
    answer = 0
    nums.sort()
    tmp = combinations(nums, 3)

    for i in tmp:
        value = sum(i)
        if check(value):
            answer += 1

    return answer