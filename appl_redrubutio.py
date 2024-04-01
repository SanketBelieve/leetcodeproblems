def max_happiness(happiness, k):
    # Sort the happiness array in descending order
    happiness.sort(reverse=True)

    totalHappiness = 0
    for i in range(k):
        if happiness:
            selected_child = happiness.pop(0)
            totalHappiness += selected_child
            # Decrement happiness of remaining children
            for j in range(len(happiness)):
                happiness[j] = max(0, happiness[j] - 1)

    return totalHappiness

# Example usage
happiness1 = [1, 2, 3]
k1 = 2
print(max_happiness(happiness1, k1))  # Output: 4