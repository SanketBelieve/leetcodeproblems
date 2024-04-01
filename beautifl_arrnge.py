from itertools import combinations
n = 2
cnt=0
s=[]
for i in range(1,n+1):
    s.append(i)
print(s) 

for i in range(len(s)+1):
    
    s.extend(combinations(s,i))
print(s)    

       