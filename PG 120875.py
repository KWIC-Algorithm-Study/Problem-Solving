def solution(dots):
    A, B, C, D = dots
    
    def parallel(p1, p2, p3, p4):
        return (p2[1]-p1[1])*(p4[0]-p3[0]) == (p4[1]-p3[1])*(p2[0]-p1[0])
    
    if parallel(A,B,C,D): 
        return 1
    if parallel(A,C,B,D):
        return 1
    if parallel(A,D,B,C):
        return 1
    else:
        return 0