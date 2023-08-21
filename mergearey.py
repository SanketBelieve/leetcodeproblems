def merge(nums1, m, nums2, n):
    ptr1 = m - 1
    ptr2 = n - 1
    ptr = m + n - 1

    while ptr1 >= 0 and ptr2 >= 0:
        if nums1[ptr1] > nums2[ptr2]:
            nums1[ptr] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[ptr] = nums2[ptr2]
            ptr2 -= 1
        ptr -= 1

    while ptr2 >= 0:
        nums1[ptr] = nums2[ptr2]
        ptr2 -= 1
        ptr -= 1

nums1 = [1, 2, 3, 0, 0, 0]  # Example nums1 array with additional space
m = 3  # Number of elements in nums1
nums2 = [2, 5, 6]  # Example nums2 array
n = 3  # Number of elements in nums2

merge(nums1, m, nums2, n)

# The merged and sorted array will be stored in nums1
print(nums1)
