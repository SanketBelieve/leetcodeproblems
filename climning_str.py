'''stairs = int(input("enter:"))
count = 0
for i in range(stairs):
  '''
  
def climbStairs( n: int) -> int:
    one , two = 1 , 1
    
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one        

s=climbStairs(5) 
print(s)
    
   