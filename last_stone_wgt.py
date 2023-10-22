# stones = [2,7,4,1,8,1]
# stones.sort()
# p=[]
# for i in range(len(stones)):
#     if len(stones)==1:
#         print(stones)
#     else:    
#         p=stones[-1]-stones[-2]
#         p.append(p)
# print(p) 
         
# def lastStoneWeight( stones: list[int]) -> int:
#     stones.sort()
    
#     while len(stones) > 1:
#         m1=max(stones)
#         stones.remove(m1)
#         m2=max(stones)
#         stones.remove(m2)
    
#         if m1 < m2:
#             m2 = m2 - m1
#             stones.append(m2)
    
#         elif m2 < m1:
#             m1 = m1 - m2
#             stones.append(m1)
    
#     if len(stones) == 0:
#         return 0
#     return stones[0]  

def lastStoneWeight(stones: list[int]) -> int:
    while len(stones) > 1:
        m1 = max(stones)
        stones.remove(m1)
        m2 = max(stones)
        if m1 > m2:
            stones.append(m1 - m2)
        elif m2 > m1:
            stones.append(m2 - m1)
        stones.remove(m2)
    return stones[0] if len(stones) == 1 else 0

s=[2,7,4,1,8,1]
print(lastStoneWeight([2,7,4,1,8,1]))

