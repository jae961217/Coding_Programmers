def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if i.isalpha() or i.isnumeric() or i in ['-', '_', '.']:
            answer += i
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer = '.'
    if answer[-1] == '.': answer = answer[:-1]

    # 5
    if answer == '': answer = 'a'

    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer