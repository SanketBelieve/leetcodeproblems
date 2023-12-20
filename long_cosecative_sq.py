nums = [100, 4, 200, 1, 3, 2]

numset=set(nums)
long=0
for i in nums:
    if (i-1) not in numset:
        length=0
        while(i+length) in numset:
            length+=1
        long=max(long,length)    
print(long)    
            
    
