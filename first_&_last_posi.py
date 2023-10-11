nums = [5,7,7,8,10]
target = 6
ls=[]
#if target not in nums:
for i in range(len(nums)):
    if target == nums[i]:
        ls.append(i)
    
print([ls[0],ls[-1]])        
        
        
        
        
        
'''        
if len(ls)==0:
    print([-1,-1])
else:    
    print(ls)'''
    