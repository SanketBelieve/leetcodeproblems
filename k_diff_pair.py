nums = [3,1,4,1,5]
k = 2
nums.sort()

cnt=0
# s=set([])
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if abs(nums[i]-nums[j])==k:
#             s.add((nums[i],nums[j]))
# print(len(s))
            
vis, ans = set(), set()
for v in nums:
    if v - k in vis:
        ans.add(v - k)
        print(ans)
    if v + k in vis:
        ans.add(v)
    vis.add(v)
print(len(ans))            