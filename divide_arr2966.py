nums = [1,3,4,8,7,9,3,5,1]
k = 2
s=[]
nums.sort()

for i in range(0,len(nums),3):
    if nums[i+2]-nums[i] > k:
        print([])
    s.append([nums[i:i+3]])
print(s)        