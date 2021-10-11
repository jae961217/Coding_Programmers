def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        num1, num2 = '', ''
        while arr1[i]:
            if arr1[i] % 2 == 0:
                num1 = ' ' + num1
            else:
                num1 = '#' + num1
            arr1[i] //= 2
        while arr2[i]:
            if arr2[i] % 2 == 0:
                num2 = ' ' + num2
            else:
                num2 = '#' + num2
            arr2[i] //= 2
        tmp = ''
        for j in range(len(num1), n):
            num1 = ' ' + num1
        for j in range(len(num2), n):
            num2 = ' ' + num2
        for j in range(len(num1)):
            if num1[j] == '#' or num2[j] == '#':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer