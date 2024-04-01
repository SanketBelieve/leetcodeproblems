a = [1,2]
b = [-2,-1]
c = [-1,2]
d = [0,2]

k=dict()
for i in a:
    for j in b:
        l=-(i+j)
        if l in k:
            k[l]+=1
        else:
            k[l]=1
count=0
for i in c:
    for j in d:
        l=i+j
        if l in k:
            count+=k[l]
print(count)                            
# for i in c:
#     for j in d:
#         print(i+j)        
