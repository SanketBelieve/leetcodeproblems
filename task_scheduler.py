tasks = ["A","A","A","B","B","B"]
n = 2
#A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
d={}
for i in tasks:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)  
lst=sorted(d.values()) 
print(lst)         
mx_no=lst[-1]
print(mx_no)
i=0
countr=0
while i<len(lst) and lst[i]==mx_no:
    countr+=1
    i+=1
res=(mx_no-1)*(n+1)+countr
print(max(len(tasks),res)) 