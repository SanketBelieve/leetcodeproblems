prices = [1,3,2,8,4,9]
n=len(prices)
fee = 2
profit=0
buy=[0]*n
sell=[0]*n
buy[0]=-prices[0]
for i in range(1,n):
    buy[i]=max(buy[i-1],sell[i-1]-prices[i])
    sell[i]=max(sell[i-1],buy[i-1]+prices[i]-fee)
print(sell[-1])    
            