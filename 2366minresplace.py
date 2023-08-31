def minimumReplacement( nums: list[int]) -> int:
    operations = 0
    prev_bound_list = nums[-1]
    for num in reversed(nums[:-1]):
        no_of_times=(num + prev_bound_list-1)//prev_bound_list
        operations += no_of_times-1
        prev_bound_list = num // no_of_times
    return operations

print(minimumReplacement([3,9,3]))    
    