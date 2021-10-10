def solution(dartResult):
    answer = 0
    score = ['S', 'D', 'T']
    num = []
    zerocheck = False
    index = 0
    for i in range(len(dartResult)):
        if dartResult[i] == '0' and zerocheck:
            zerocheck = False
            continue
        if dartResult[i].isnumeric():
            if dartResult[i] == '1' and dartResult[i + 1] == '0':
                zerocheck = True
                num.append(10)
            else:
                num.append(int(float(dartResult[i])))
            index += 1
        elif dartResult[i] in score:
            tmp = num[-1]
            num[-1] = tmp ** (score.index(dartResult[i]) + 1)
            answer += num[-1]
        elif dartResult[i] in ['#', '*']:
            if dartResult[i] == '#':
                num[-1] *= -1
                answer += 2 * num[-1]
            else:
                if not index == 1:
                    answer += num[-2]
                    num[-2] *= 2
                answer += num[-1]
                num[-1] *= 2
        print(dartResult[i], answer)

    return answer