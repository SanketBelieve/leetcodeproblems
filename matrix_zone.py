def max_distinct_count(arr1, arr2, k):
    # Sort the arrays in ascending order
    arr1.sort()
    arr2.sort(reverse=True)

    i = 0
    j = 0

    # Perform swapping operations while there are available swaps and elements in both arrays
    while k > 0 and i < len(arr1) and j < len(arr2):
        # If the element in arr2 is greater, swap elements
        if arr2[j] > arr1[i]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
            k -= 1
        else:
            break

    # Count the distinct elements in the modified arr1
    distinct_count = len(set(arr1))

    return distinct_count

# Example usage
arr1 =[2,3,3,2,2]
arr2 = [1,3,2,4,1]
k = 2

result = max_distinct_count(arr1, arr2, k)
print("Maximum count of distinct elements:", result)
print("Modified arr1:", arr1)
