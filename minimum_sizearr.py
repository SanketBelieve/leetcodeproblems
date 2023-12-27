target = 7
nums = [1,4,4]
res=float("inf")
l,total=0,0
for r in range(len(nums)):
    total+=r
    while total>=target:
        res=min(r-l+1,total)
        total-=nums[l]
        l+=1
print(res)        
        

