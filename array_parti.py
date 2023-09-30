nums = [1,4,3,2]
nums.sort()
print(nums)

tot=0
for i in range(len(nums)):
    print(i)
    if i%2==0:
        tot+=nums[i]
print(tot)


