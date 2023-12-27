s = "leetcode"
wordDict = ["leet","code"]

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

dp = [True] + [False] * (len(s))
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j+1] in wordDict:
            dp[j+1] = dp[i] or dp[j+1]
print(dp[-1])