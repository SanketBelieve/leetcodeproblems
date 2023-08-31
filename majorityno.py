def majorityElement(self, nums: list[int]) -> int:
    return sorted(nums)[len(sorted(nums))//2]
    