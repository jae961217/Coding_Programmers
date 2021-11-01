def solution(enroll, referral, seller, amount):
    answer = []

    human = {}
    money = {}
    for i in range(len(enroll)):
        money[enroll[i]] = 0
        if referral[i] == '-':
            human[enroll[i]] = 'center'
        else:
            human[enroll[i]] = referral[i]

    for i in range(len(seller)):
        value = amount[i] * 100
        tmp = seller[i]
        while tmp != 'center':
            if value < 10:
                money[tmp] += value
                break
            else:
                money[tmp] += (value - int(value / 10))
                value //= 10
                tmp = human[tmp]

    for i in money:
        answer.append(money[i])
    return answer