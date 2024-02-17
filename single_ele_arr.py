nums = [1,1,2,3,3,4,4,8,8]
s={}
for i in nums:
    
    if i in s:
        s[i]+=1
    else:
        s[i]=1    
print(s)       
for i,c in s.items():
    if c==1:
        print(i)