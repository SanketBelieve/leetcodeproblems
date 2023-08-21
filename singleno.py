# Taking input as a string
input_string = input("Enter values separated by spaces: ")

# Splitting the input string into a list
input_list = input_string.split()

# Converting elements to integers (if needed)
input_list = [int(x) for x in input_list]

print("Input list:", input_list)
