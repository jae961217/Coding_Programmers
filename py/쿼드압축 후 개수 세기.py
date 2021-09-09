def solution(arr):
    answer = [0, 0]

    def func(a, b, cnt):
        tmp = arr[a][b]
        flag=False

        for i in range(cnt):
            for j in range(cnt):
                if not tmp==arr[a+i][b+j]:
                    flag=True
                    break
            if flag:
                break

        if flag:
            func(a, b, cnt // 2)
            func(a + cnt // 2, b, cnt // 2)
            func(a, b + cnt // 2, cnt // 2)
            func(a + cnt // 2, b + cnt // 2, cnt // 2)
        else:
            answer[tmp]+=1

    func(0, 0, len(arr))
    return answer