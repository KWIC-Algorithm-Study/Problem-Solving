def solution(n):
    x,y=1,1    
    for i in range(1,n):
        t=(x+y)%1000000007
        x,y=y,t
    return y