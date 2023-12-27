path="NESWW"
s=[]
cnt1=0
cnt2=0
for i in range(len(path)):
    if path[i]=='N' or path[i]=='W':
       s.append(1) 
    elif path[i]=='E' or path[i]=='S':
        
        s.append(-1)
for i in range(len(s)):
    if s[i]==1:
        cnt1+=1  
    else:
        cnt2=1               
if cnt1>cnt2:
    print(True)  
else:
    print(False)             