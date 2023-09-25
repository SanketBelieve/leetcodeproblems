def arrangeCoins(self, n: int) -> int:
    
    total =1
    row = 1
    while total <= n:
        total = total+row+1
        row+=1
    return row-1    
        
        
    
