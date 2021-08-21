def solution(record):
    answer = []
    id = dict()
    for i in record:
        tmp = i.split()
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            id[tmp[1]] = tmp[2]

    for i in record:
        tmp = i.split()
        value = ''
        if tmp[0] == 'Enter':
            value = id[tmp[1]] + '님이 들어왔습니다.'
        elif tmp[0] == 'Leave':
            value = id[tmp[1]] + '님이 나갔습니다.'
        else:
            continue
        answer.append(value)

    return answer