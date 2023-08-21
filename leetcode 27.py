'''
def removeelement(nums,val):
    if len(nums)==0:
        return 0
    
    i=0
    for j in range(len(nums)):
        if nums[j]!=val:
            nums[i] = nums[j]
            i+=1
    
    return i       

nums = [0,1,2,2,3,0,4,2]
val= 2
print(removeelement(nums,val))  # Output: 5
print(nums)
'''
def removeElement(nums, val):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1

    return i
nums = [0,1,2,2,3,0,4,2]
val = 0
print(removeElement(nums, val))
print(nums)
