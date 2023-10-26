nums = [4,1,2,3]
s=[]
p=[]
ans=[]
for i in range(len(nums)):
    if i%2==0:
        s.append(nums[i])
    if i%2==1:
        p.append(i)    
s.sort()
print(s)
print(p)      
n=sorted(p, reverse=True)
print(n)

for a,b in zip(s,n):
    ans.append(a)
    ans.append(b)
print(ans)
            
def sortEvenOdd(nums: list[int]) -> list[int]:
        s=[]
        p=[]
        d=[]
        f=[]
        cst=[0]*len(nums)
        for i in range(len(nums)):
            if i%2==0:
                s.append(nums[i])
                d.append(i)
            if i%2==1:
                p.append(nums[i])  
                f.append(i)  
        s.sort()
        p.sort()      
        p=p[::-1]

        for i in range(len(s)):
            cst[d[i]]=s[i]
        for j in range(len(p)):
            cst[f[j]]=p[j]
        return cst