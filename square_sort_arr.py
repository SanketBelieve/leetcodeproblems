nums = [-4,-1,0,3,10]
s=[]
for i in range(len(nums)):
    s.append(nums[i]*nums[i])
print(sorted(s))   