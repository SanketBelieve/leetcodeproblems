prices = [7,1,5,3,6,4]
ans=[]
for i in range(len(prices)-1):
    for j in range(i,len(prices)-1):
        m=prices[j]-prices[i]
        ans.append(m)

print(max(ans))        