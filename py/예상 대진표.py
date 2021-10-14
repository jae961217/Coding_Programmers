def solution(n,a,b):
    answer = 1

    while True:
        if max(a,b)==min(a,b)+1 and max(a,b)%2==0:
            break
        a+=1
        b+=1
        a//=2
        b//=2
        answer+=1

    return answer