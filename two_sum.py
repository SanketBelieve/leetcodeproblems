nums = [3,2,4]
target = 6
l=[]
for i in range(len(nums)):
    #print(i)
    for j in range(i+1,len(nums)):
        print(j)

        if nums[i]+nums[j]==target:
            l.append(i)
            l.append(j)
print(l)      
        