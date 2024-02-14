nums = [1,1,1,2,2,3]
k = 2

count = Counter(nums)
sortedC = dict(sorted(count.items(), key=lambda x:-x[1]))
ans = []
for i, v in sortedC.items():
    if k > 0 and i not in ans:
        ans.append(i)
        k -= 1
# print(ans)
print(ans)
    
