nums = [-4,-1,0,3,10]
p=[]
s=[]
for i in nums:
    p.append(abs(i))
p.sort()
for j in p: 
    s.append(j*j)
print(s)    
       
# for i in nums:
#     s=i*i
#     print(s)
    