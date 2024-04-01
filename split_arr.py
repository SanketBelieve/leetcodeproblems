#nput: nums = [1,1,2,2,3,4]
#Output: true
# #Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].
# n=[1,1,2,2,3,4]
# n.sort()
# s=[]
# p=[]
# for i in range(len(n)-1):
#     if i < len(n) // 2:
#         s.append(n[i])
#     else:
#         p.append(n[i])

# print(s)
# print(p)   
# if s!=p:
#     print(True)
# if len(n)%2==0:
#     for i in range(len)

def canSplit(nums):
    # Count occurrences of each element in the array
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Check if there are more than n/2 unique elements
    unique_elements = len(count)
    # if unique_elements > len(nums) // 2:
    #     return False
    
    # Check if any element has more than 2 occurrences
    for num in count:
        if count[num] > 2:
            return False
    
    return True

# Example usage:
nums1 = [1, 1, 2, 2, 3, 4]
nums2 = [1, 1, 1, 1]

print(canSplit(nums1))  # Output: True
print(canSplit(nums2))  # Output: False
