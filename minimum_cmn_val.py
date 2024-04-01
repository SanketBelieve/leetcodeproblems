n1=[6,13,18,18,28,34,37,39,46,50,52,54,62,63,65,66,75,80,97,98]
n2=[10,13,13,19,27,33,40,41,43,46,56,61,69,72,78,79,82,88,91,94] 


# if min(nums1)>min(nums2) and min(nums1) in nums2:
#     print(min(nums1))
# elif min(nums2)>min(nums1) and min(nums2) in nums1:
#     print(min(nums2))    
# elif min(nums1)==min(nums2):
#     print(min(nums1))
nums1 = set(n1)
nums2 = set(n2)

common_min = nums1.intersection(nums2)
print(common_min)
if common_min:
    print(min(common_min))
else:
    print("No common minimum value")