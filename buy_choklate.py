prices = [98,54,6,34,66,63,52,39]
money = 62
prices.sort()
for i in range(len(prices)-1):
    if prices[i]+prices[i+1]<=money:
        print(money-(prices[i]+prices[i+1]))
        break  
    else:
        print(money)