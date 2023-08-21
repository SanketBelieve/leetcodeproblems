def primef(num:int):
    if num == 1:
        return [1]
    factor = []
    n = 2
    while n**2<=num:
        if num % n==0:
            factor.append(n)
            num //=n
        else:
            n+=1
    if num>1:
        factor.append(num)
    return factor    
 
print(primef(24))        
        
       