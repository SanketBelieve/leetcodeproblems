nums=[1,12,1,2,5,50,3]
s=[]
p=0
nums.sort()
n = len(nums)
for i in range(n-1,-1,-1):
    print(i)
    val = sum(nums[0:i])
    print(val)
    if n >= 3 and nums[i] < val:
        print(nums[i] + val)
print(-1)     