nums=[3,3,5,5]
nums.sort()
product1 = nums[-1] * nums[-2] * nums[-3]
product2 = nums[0] * nums[1] * nums[-1]
print(product1)
print(product2)


arr = [1, 5, 6, 8, 5, 6]

# Initialize a variable to store the product
product = 1

# Iterate through the elements and multiply them together
for num in arr:
    product *= num

# Print the result
print("The product of the array elements is:", product)