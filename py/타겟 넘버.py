answer = 0


def solution(numbers, target):
    global answer
    size = len(numbers)

    def func(index, value):
        global answer
        if index == size:
            if value == target:
                answer += 1
            return

        func(index + 1, value + numbers[index])
        func(index + 1, value - numbers[index])

    func(0, 0)

    return answer