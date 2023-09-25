def thirdMax(nums: list[int]) -> int:
    lst=list(sorted(set(nums)))
    try:
        return lst[-3]
    except:
        return lst[-1]
    
print(thirdMax[1,2,3,5])    