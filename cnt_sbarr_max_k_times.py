nums = [1, 3, 2, 3, 3]
k = 2
m = max(nums)
cnt=0
# sublists = []
# n = len(nums)
# for i in range(n):
#     for j in range(i+1, n+1):
#         sublists.append(nums[i:j])
# print("All sublists:", sublists)
# print("Number of sublists:", len(sublists))

# for sublist in sublists:
#     if sublist.count(m) >= k:
#         cnt+=1
# print(cnt)        
l=0
ans=0
for r,num in enumerate(nums):
    if num==m:
        cnt+=1
    while cnt==k:
        if nums[l]==m:
            cnt-=1
        l+=1
    ans+=l       
print(ans)            
        
        
        