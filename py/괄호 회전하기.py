def solution(s):
    answer = 0

    def check(s):
        cnt=[0,0,0]
        for i in range(len(s)):
            if i==len(s)-1 and s[i] in ['[','(','{']:
                return False
            if s[i]=='[':
                cnt[0]+=1
                if s[i+1] in [')','}']:
                    return False
            elif s[i]=='{':
                cnt[1]+=1
                if s[i+1] in [')',']']:
                    return False
            elif s[i]=='(':
                cnt[2]+=1
                if s[i+1] in ['}',']']:
                    return False
            elif s[i] in [']','}',')']:
                if cnt[[']','}',')'].index(s[i])]==0:
                    return False
                cnt[[']','}',')'].index(s[i])]-=1
        for i in cnt:
            if not i==0:
                return False
        return True

    for i in range(len(s)):
        if check(s):
            answer+=1
        s=s[1:]+s[0]

    return answer