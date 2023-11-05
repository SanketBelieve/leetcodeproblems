nums = [12,345,2,6,7896]
count=0
for i in nums:
    if len(str(i))%2==0:
        count+=1
print(count)