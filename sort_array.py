nums = [3,1,2,4]
s=[]
p=[]
for i in nums:
    if i%2==0:
        s.append(i)

for j in nums:
    if j%2!=0:
        p.append(j)
    
print(s)    
print(p)
print(s+p)