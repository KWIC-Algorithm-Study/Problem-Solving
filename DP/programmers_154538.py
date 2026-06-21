def solution(x, y, n):
    dp=[[x,0]]
    i=0
    s=set()
    s.add(x)
    if x==y:
        return 0
    while True:
        if len(dp)-i<1:
            return -1
        plus,mult_2,mult_3=dp[i][0]+n,dp[i][0]*2,dp[i][0]*3
        
        if plus==y or mult_2==y or mult_3==y:
            return dp[i][1]+1
        
        if plus<=y and plus not in s:
            dp.append([plus,dp[i][1]+1])
            s.add(plus)
        if mult_2<=y and mult_2 not in s:
            dp.append([mult_2,dp[i][1]+1])
            s.add(mult_2)
        if mult_3<=y and mult_3 not in s:
            dp.append([mult_3,dp[i][1]+1])
            s.add(mult_3)
        
        i+=1