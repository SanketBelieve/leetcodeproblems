nums = [1,17,5,10,13,15,10,5,16,8]
dp=[nums[i-1]-nums[i] for i in range(1,len(nums)) if nums[i-1]-nums[i]!=0]
if not dp:
    print(1)
curr=2    
for i in range(1,len(dp)):
    if nums[i-1]>0 and nums[i]<0 or nums[i-1]<0 and nums[i]>0:
        curr+=1
print(curr)        
           

    
# [1,17,5,10,13,15,10,5,16,8]
# [16, -12, 5, 3, 2, -5, -5, 11, -8]
# [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
# (16, -7, 3, -3, 6, -8)
