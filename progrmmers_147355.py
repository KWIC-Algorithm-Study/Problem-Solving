def solution(t, p):
    answer = 0
    t_len=len(t) #7
    p_len=len(p) #3
    
    for i in range(t_len-p_len):
        if int(t[i:i+p_len])<=int(p):
            answer+=1
    
    return answer