'''def isMonotonic(nums: list[int]) -> bool:
    for i in nums:
        for j in nums:
            if i <= j  :
                return True
            if i >= j :
                return True
            else:
                return False
print(isMonotonic([1,3,2]))'''
def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return True
        direction = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                if direction == 0:
                    direction = 1
                elif direction == -1:
                    return False
            elif nums[i] < nums[i-1]:  # decreasing
                if direction == 0:
                    direction = -1
                elif direction == 1:
                    return False
        
        return True
