n = 12
l=[]
dp=[n]*(n+1)
dp[0]=0
for target in range(1,n+1):
    for s in range(1,target):
        square = s*s
        if target - square < 0:
            break
        dp[target]=min(dp[target],1+dp[target-square])   
print(dp[n])
