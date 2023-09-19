nums = [1,2,3,1,2,3]
k = 2

for i in range (len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i]==nums[j] and abs(i-j)<=k:
            print(True)
        else:
            print(False)  


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(d[nums[i]] - i) <= k:
                    return True
            d[nums[i]] = i
        return False             

            
    