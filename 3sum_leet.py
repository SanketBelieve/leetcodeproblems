'''
def threeSum(self, nums: list[int]) -> list[list[int]]:
    n=len(nums)
    nums.sort()
    res=[]
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j , k = i+1 ,n-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s==0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif s < 0:
                j += 1
            else:
                k -= 1
    return res
#nums = [-1, 0, 1, 2, -1, -4]
print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
# '''
# def three_sum(nums):
#     n = len(nums)
#     nums.sort()
#     res = []
#     for i in range(n - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         j, k = i + 1, n - 1
#         while j < k:
#             s = nums[i] + nums[j] + nums[k]
#             if s == 0:
#                 res.append([nums[i], nums[j], nums[k]])
#                 j += 1
#                 k -= 1
#                 while j < k and nums[j] == nums[j - 1]:
#                     j += 1
#                 while j < k and nums[k] == nums[k + 1]:
#                     k -= 1
#             elif s < 0:
#                 j += 1
#             else:
#                 k -= 1
#     return res
# nums = [-1, 0, 1, 2, -1, -4]
# print(three_sum(nums))  # [[-1, -1, 2], [-1, 0, 1]]


# nums.sort()
# l=[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+3,len(nums)):
#             if nums[i]+nums[j]+nums[k]==0:
#                 l.append([nums[i],nums[j],nums[k]])

# print(l)                
                
nums = [-1,0,1,2,-1,-4]
res=[]
nums.sort()
for i,a in enumerate(nums):
    if a > 0 or a==nums[i-1]:
        continue
    l,r=i+1,len(nums)-1
    while l<r:
        threesum=a+nums[l]+nums[r] 
        if threesum>0:
            r -= 1
        elif threesum <0:
            l += 1
        else:
            res.append([a,nums[l],nums[r]])
            while nums[l]==nums[l-1] and l < r:
                l+=1
print(res)            
       
            
            