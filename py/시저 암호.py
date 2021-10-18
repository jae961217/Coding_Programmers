def solution(s, n):
    answer = ''
    size = 26
    low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

    for i in s:
        if i == ' ':
            answer += ' '
        elif i in low:
            value = low.index(i)
            answer += low[(value + n) % size]
        elif i in up:
            value = up.index(i)
            answer += up[(value + n) % size]
    return answer