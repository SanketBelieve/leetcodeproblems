nums = [4,2,5,7]
ls=[]
ls1=[]
ans=[]
for i in nums:
    if i%2==0:
        ls.append(i)
    if i%2==1:
        ls1.append(i)
print(ls)        
print(ls1)
for a,b in zip(ls,ls1):
    ans.append(a)
    ans.append(b)
print(ans)    
    
