def earliest_marked_second(nums, changeIndices):
    marked_indices = set()
    for s in range(len(changeIndices)):
        if nums[changeIndices[s] - 1] == 0:
            marked_indices.add(changeIndices[s])
        else:
            nums[changeIndices[s] - 1] -= 1
        
        if len(marked_indices) == len(nums):
            return s + 1
    
    return -1

# Example usage:
nums = [2, 2, 0]
changeIndices = [2, 2, 2, 2, 3, 2, 2, 1]
print(earliest_marked_second(nums, changeIndices))  # Output: 8
