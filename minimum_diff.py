arr=[4,2,1,3]
p=[]
for i in range(1,len(arr)):
    print(i)
    diff=arr[i]-arr[i-1]
    p.append(diff)    
print(p)    

def minimumAbsDifference( arr: list[int]) -> list[list[int]]:
    arr.sort()  # Sort the array in ascending order
    min_diff = float('inf')  # Initialize the minimum difference to infinity
    result = []

    # Calculate the minimum difference
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff

    # Find pairs with the minimum difference
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff == min_diff:
            result.append([arr[i-1], arr[i]])

    return result