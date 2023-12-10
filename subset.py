from itertools import combinations

def generate_subsets(input_list):
    subsets = []
    for r in range(len(input_list) + 1):
        subsets.extend(combinations(input_list, r))
    return subsets

# Example usage:
my_list = [1, 2, 3]
result = generate_subsets(my_list)

# Print the result
for subset in result:
    print(subset)
