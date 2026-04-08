n=int(input())
lst=list(map(int,input().split()))

dp=[0]*n
dp[0]=lst[0]

for i in range(1,n):
    m=0
    for j in range(i//2+1):
        if m<dp[i-j-1]+dp[j]:
            m=dp[i-j-1]+dp[j]
    dp[i]=max(lst[i],m)
print(max(dp))


# for i in range(1,n):
#     for j in range(i):
#        dp[i]=max(lst[i], dp[i-j-1]+dp[j], dp[i])
# print(max(dp))
