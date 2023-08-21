#a=int(input())
#b= a % 2
#print(b)
'''
a=(1+25)//2
print(a)
s=a-1
print(s)
'''

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    
    start = 1
    end = x
    
    while start <= end:
        mid = (start + end) // 2
        
        if mid * mid > x:
            end = mid - 1
        else:
            start = mid + 1
    
    return start - 1
m=mySqrt(55)
print(m)

