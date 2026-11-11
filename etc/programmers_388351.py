def solution(sche, timelog, startday):
    answer=0
    newlog=[]
    for i in range(len(sche)):
        newlog.append(timelog[i][-startday+1:] + timelog[i][:-startday+1])
        
    new_sche=[]
    for i in sche:
        if int(str(i+10)[-2])==6:
            new_sche.append(i+50)
        else:
            new_sche.append(i+10)
            
    
    for i in range(len(sche)):
        cnt=0
        for j in range(0,5):
                
            if newlog[i][j]<=new_sche[i]:
                cnt+=1
        if cnt==5:
            answer+=1
    return answer
