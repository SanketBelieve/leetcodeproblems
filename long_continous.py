nums = [2,2,2,2]
l=0
for i in range(len(nums)-1):
    if nums[i]<nums[i+1]:
        l+=1   
print(l)  

def findLengthOfLCIS( nums: list[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        l=1
        c=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                l+=1
                c=max(c,l)
            else:
                l=1    
              
        return c      
    