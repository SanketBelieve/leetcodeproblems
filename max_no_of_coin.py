def maxCoins(self, piles: list[int]) -> int:
    piles.sort()
    i,j=0,len(piles)-1
    total = 0
    while i < j:
        total += piles[j-1]
        i+=1
        j-=2
    return total    
            
piles = [2,4,1,2,7,8]
piles.sort()
np=[1, 2, 2, 4, 7, 8]
print(piles)
j=len(piles)-1
print(j)
p=piles[j-1]
print(p)
            