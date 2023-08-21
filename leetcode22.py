'''
'''
'''
def removeduplicate(nums:list[0]):
    if not nums:
        return 0
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[j]=nums[i]
    return i+1

nums=[1,1,2,3,3,5,6]
print(removeduplicate(nums))
print(nums[:6])
     '''
     
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1

    return i


nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print(removeDuplicates(nums))  # Output: 5
print(nums[:5])  # Output: [1, 2, 3, 4, 5]
   
            
        