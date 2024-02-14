nums = [1,3,4,1,2,3,1]
nums.sort()
s=[]
p=[]
for i in range(len(nums)-1,-1,-1):
    if nums[i]!=nums[i-1]:
        s.append(nums[i])
    elif nums[i]==nums[i-1]:
        p.append(nums[i])
            
print(s)
print(p)