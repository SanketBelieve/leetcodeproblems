nums = [4,6,7,7]
s=[]
for i in range(len(nums)-1):
    if nums[i+1]>nums[i]:
        s.append([nums[i],nums[i+1]])
print(s)   