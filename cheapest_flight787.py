n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

prices=[float('inf')]*n
prices[src]=0
for i in range(k+1):
    tempP=prices.copy()
    for s,d,p in flights:
        if prices[0]==float('inf'):
            continue
        if prices[s]+p < tempP[d]:
            tempP[d]= prices[s]+p
    prices=tempP
if prices[dst]==float('inf'):
    print(-1)
else:
    print(prices[dst])        