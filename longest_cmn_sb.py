text1 = "ezupkr"
text2 = "ubmrapg" 
cnt=0
# for i in range((len(text1))):
#     print(text1[i])
# for j in range(len(text2)):
#     print(text2[j]) 
# if text1[i]==text2[j]:
#     cnt+=1
# print(cnt)        
          
# for i in range(len(text1)):
#     if text1[i] in text2:
#         cnt+=1
# print(cnt)                 

m,n=len(text1),len(text2)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    ans=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max((dp[i][j-1]),dp[i-1][j])
            ans=max(ans,dp[i][j])
    return ans