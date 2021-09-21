def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []

    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            s1.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            s2.append(str2[i:i + 2])

    for i in s1:
        if i in s2:
            s2.remove(i)
            answer += 1

    tmp = len(s1) + len(s2)

    if answer == 0 and tmp == 0:
        answer = 65536
    else:
        answer *= 65536
        answer //= tmp

    return answer