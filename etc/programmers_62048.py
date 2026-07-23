def solution(w,h):
    gcd=1
    for i in range(min(w,h),0,-1):
        if w%i==0 and h%i==0:
            gcd=i
            break
    
    return w * h -(w+h-gcd) 