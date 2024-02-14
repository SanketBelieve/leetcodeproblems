
def maximumGap( nums: list[int]) -> int:
    s=[]
    nums.sort()
    if len(nums)==0:
        return 0
          
    for i in range(len(nums)-1):
        s.append(nums[i+1]-nums[i])
    return max(s)

nums=[3,6,9,1]
print(maximumGap(nums))