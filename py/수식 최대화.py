def solution(expression):
    answer = 0

    op = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]

    def cal(pri, n, ex):
        if n == 2:
            return str(eval(ex))
        if pri[n] == '*':
            res = eval('*'.join([cal(pri, n + 1, e) for e in ex.split('*')]))
        if pri[n] == '+':
            res = eval('+'.join([cal(pri, n + 1, e) for e in ex.split('+')]))
        if pri[n] == '-':
            res = eval('-'.join([cal(pri, n + 1, e) for e in ex.split('-')]))
        return str(res)

    for i in op:
        answer = max(answer, abs(int(cal(i, 0, expression))))

    return answer