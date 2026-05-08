def solution(n, lost, reserve):
    s=[0]*(n+2)
    lost.sort()
    reserve.sort()
    
    over=[]
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            over.append(i)
    
    for i in over:
        if i in lost:
            lost.remove(i)
    
    for i in lost:
        s[i]=1
        
    
    answer=n-len(lost)
    for i in reserve:
        if s[i-1]==1:
            s[i-1]=0
            answer+=1
            continue
            
        elif s[i+1]==1:
            s[i+1]=0
            answer+=1
    
    return answer