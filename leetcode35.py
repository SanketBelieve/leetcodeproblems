#def searchInsert( nums: list[int], target: int) -> int:
'''    
my_list = [1,2,3,4]
element = 2

if element in my_list:
    index = my_list.index(element)
    print(f"The element '{element}' is at index {index}")
else:
    print(f"The element '{element}' is not found in the list")
'''
def searchInsert(nums: list[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1
        return l        
              
nums = [1, 3, 5, 6,7]
target = 0
index = searchInsert(nums, target)
print(index)
