nums = [1,2,3,4,5]
nums.sort()
d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1    
print(d)
cnt=0
p=max(d.values())
for i,v in d.items():
    if p==v:
        cnt+=1 
print(cnt*p)
#for i,v in d.items():
          
# for i,v in d.items
        