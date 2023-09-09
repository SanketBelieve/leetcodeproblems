def combinationSum4(nums: list[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target+1)
        for i in range(target+1):
            for num in nums:
                if num > i: continue
                elif num == i: dp[i] += 1
                else: dp[i] += dp[i - num]
        return dp[target]