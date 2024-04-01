lo = 7
hi = 11
k = 2
l=[]
n=[i for i in range(lo,hi+1)]
for i in range(lo,hi+1):
    steps = 0
    while i != 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
        steps += 1
        
    l.append(steps)
print([x for _, x in sorted(zip(l,n))][k-1])    

# # Example usage:
power_array = []
for i in range(lo, hi + 1):
    steps = 0
    while i != 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
        steps += 1
    power_array.append(steps)

# Sort the interval based on the power array
sorted_interval = sorted(zip(power_array, range(lo, hi + 1)))

# Extract the kth element from the sorted interval
result = sorted_interval[k - 1][1]

print(result)