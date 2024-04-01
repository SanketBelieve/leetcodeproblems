s='cabaabac'
l=0
r=len(s)-1
while l<r and s[l]==s[r]:
    c=s[l]
    while l<=r and s[l]==c:
        l+=1
    while r>l and s[r]==c: 
        r-=1
print(c)        
print(r-l+1)