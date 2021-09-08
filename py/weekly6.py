def solution(weights, head2head):
    answer = []
    tmp=[]
    for i in range(len(head2head)):
        win, lose=0,0
        heavy_win=0
        for j in range(len(head2head[i])):
            if head2head[i][j]=="N":
                continue
            elif head2head[i][j]=='W':
                win+=1
                if weights[i]<weights[j]:
                    heavy_win+=1
            elif head2head[i][j]=='L':
                lose+=1
        if win+lose==0:
            tmp.append((0,heavy_win,i))
        else:
            tmp.append((win/(win+lose),heavy_win,i))
    tmp=sorted(tmp, key=lambda x:(-x[0],-x[1],-weights[x[2]],x[2]))
    for i in tmp:
        answer.append(i[2]+1)
    return answer