nums = [23,2,4,6,6]
k = 7

for i in range(len(nums)-1):
    if nums[i]+nums[i+1]==k:
        print(True)
    elif sum(nums)%k==0:
        print(True)
    else:
        print(False)        

for i in range(len(nums)):
    sum+=nums[i]
    
    if sum%k not in hash:
        hash[sum%k]=i+1
    elif hash[sum%k] < i :    
        return True  
return False


