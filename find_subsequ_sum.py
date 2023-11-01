nums = [2,1,3,3]
k = 2

def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        val_and_index = sorted([(num, i) for i, num in enumerate(nums)])
        return [num for num, i in sorted(val_and_index[-k :], key=lambda x: x[1])]        


        