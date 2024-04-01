#nums = [1,10,2,9]
# nums=[1,2,3]
# count=0
# mein_num=min(nums)
# print(med_num)
# for i in nums:
#     print(abs(min_num-i))
#     count+=abs(min_num-i)
# print(count)    
#2nd Question
#nums = [1,10,2,9]
nums=[1,0,0,8,6]
nums.sort()
count=0
med_num=nums[len(nums)//2]
print(med_num)
for i in nums:
    print(abs(med_num-i))
    count+=abs(med_num-i)
print(count)
