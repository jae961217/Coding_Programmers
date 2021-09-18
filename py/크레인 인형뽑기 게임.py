def solution(board, moves):
    answer = 0
    tmp = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                continue
            tmp.append(board[j][i - 1])
            board[j][i - 1] = 0
            break
        if len(tmp) >= 2 and tmp[-1] == tmp[-2]:
            answer += 2
            del tmp[-1]
            del tmp[-1]

    return answer