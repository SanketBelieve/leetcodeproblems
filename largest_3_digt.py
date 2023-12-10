# num = "6777133339"
# s=""
# for i in range(len(num)-1):
#     if num[i]==num[i+1]:
#         s+=num[i]
# print(s)  
num = "6777133339"      
count=0
prev='X'
maxd=' '
for c in num:
    if c==prev: count+=1
    else: count=1
    if count==3: maxd=max(c, maxd)
    prev=c

print(maxd*3)    


