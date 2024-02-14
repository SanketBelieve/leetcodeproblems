# low = 100
# high = 300
# result = []
# for num in range(1, 10):
#     current = next_digit = num
    
#     while current <= high and next_digit < 10:
#         if current >= low:
#             result.append(current)    
#         next_digit += 1
#         current = current * 10 + next_digit
        
# # print(sorted(result))
# strs =["eat","tea","tan","ate","nat","bat"]
# #print(sorted(strs))
# print("".join(sorted(strs)))
nums = [1,2]
s=[]
nums.sort()
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        s.append(nums[i])
print(s)    