nums = [1,2,1]
for i in range(len(nums)):
    for j in range(i+1,len(nums))  :
        if nums[j] > nums[i]:
            print(nums[j])