nums = [1,2,2]

for i in nums:
    #print(i)
    cnt=0
    for j in nums:
        #print(j)
        if i==j:
            cnt+=1
print(cnt)