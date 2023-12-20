prices = [3,3,5,0,0,3,1,4]
if not prices:
    print(0)

# initialize variables for first buy, first sell, second buy, and second sell
buy1, buy2 = float('inf'), float('inf')
sell1, sell2 = 0, 0

# iterate over prices to update buy and sell values
for price in prices:
    # update first buy and sell values
    buy1 = min(buy1, price)
    sell1 = max(sell1, price - buy1)
    # update second buy and sell values
    buy2 = min(buy2, price - sell1)
    sell2 = max(sell2, price - buy2)

print(sell2) 