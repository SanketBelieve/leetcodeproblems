nums = [2,1,4,3]
left = 2
right = 3
l=[]
for i in range(len(nums)):
    if nums[i]>=left and nums[i] <=right:
        l.append(nums[i])
    elif nums[i]-nums[i+1] ==1:
        l.append([nums[i],nums[i+1]]) 
print(l)       