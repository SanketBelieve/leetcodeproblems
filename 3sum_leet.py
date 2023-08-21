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
'''
def three_sum(nums):
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == 0:
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
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # [[-1, -1, 2], [-1, 0, 1]]
           
            
            