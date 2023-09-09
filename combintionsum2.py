import itertools

def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    
    # Use itertools.combinations to generate combinations
    for i in range(1, len(candidates) + 1):
        for combo in itertools.combinations(candidates, i):
            if sum(combo) == target:
                result.append(list(combo))
    
    return result

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
output = combinationSum2(candidates, target)
print(output)
