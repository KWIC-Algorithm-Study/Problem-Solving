def solution(n, s):
    if s<n:
        return [-1]
    
    elif s%n==0:
        return [s//n]*n
    
    else:
        lst=[]
        for i in range(n,0,-1):
            x=s//i
            lst.append(x)
            s-=x
        return lst