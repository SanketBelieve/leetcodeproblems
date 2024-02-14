nums = [2,3,0,1,4]
cnt=0
r=0
l=0
for i in range(len(nums)-1):
   
    r=max(r,i+nums[i+1])
    if i==l:
        l=r
        cnt+=1
print(cnt)        