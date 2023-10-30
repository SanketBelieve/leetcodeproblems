s = "IDID"
p=[]
a=0
n=len(s)
for i in s:
    if i=='I':
        p.append(a)
        a+=0
    else:
        p.append(n)
        n-=1
if s[len(s)-1]=='I':
    p.append(n)
else:
    p.append(a)
print(p)            




