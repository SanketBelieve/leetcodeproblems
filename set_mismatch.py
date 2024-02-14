nums = [1,2,2,4]
li=[]
out=[]
for i in range(1,len(nums)+1):
    li.append(i)   
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        out.append(nums[i+1])
        out.append(li[i+1])
print(out)    
       