def findDuplicate( nums: list[int]) -> int:
    for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]
            return len(nums)
        