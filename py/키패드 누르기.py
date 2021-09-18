def solution(numbers, hand):
    answer = ''

    left, right = 10, 12
    xy = dict()

    for i in range(1, 13):
        if i % 3 == 0:
            xy[i] = [i // 3 - 1, 3]
        else:
            xy[i] = [i // 3, i % 3]

    for i in numbers:
        tmp = i
        if i == 0:
            tmp = 11
        if i in [1, 4, 7]:
            left = i
            answer += 'L'
        elif i in [3, 6, 9]:
            right = i
            answer += 'R'
        else:
            disti = xy[tmp]
            distr = xy[right]
            distl = xy[left]
            tmp1 = abs(disti[0] - distr[0]) + abs(disti[1] - distr[1])
            tmp2 = abs(disti[0] - distl[0]) + abs(disti[1] - distl[1])
            if tmp1 < tmp2:
                right = tmp
                answer += 'R'
            elif tmp1 > tmp2:
                left = tmp
                answer += 'L'
            else:
                if hand == 'right':
                    right = tmp
                    answer += 'R'
                else:
                    left = tmp
                    answer += 'L'

    return answer