nums = [3,4,-1,1]
m=min(nums)
mx=max(nums,default=0)
d={}
for num in nums:
    d[num]=True
for i in range(1,mx):
    if i not in d:
        print(i)
if mx<0:
    print(1)
else:
    print(mx+1)        