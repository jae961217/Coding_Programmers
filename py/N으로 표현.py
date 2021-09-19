def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break
        print(numbers)
        dp.append(numbers)

    return answer