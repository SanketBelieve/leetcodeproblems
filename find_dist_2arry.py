arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
# cnt=0

# for i in arr1:
    
#     for j in range(len(arr2)):
#         if i-arr2[j]==d:
#             cnt+=1
      
# print(cnt)        
x=0
for i in arr1:
    c=1
    for j in arr2:
        if abs(i-j)<=d:
            c=0
            break 
    if c:
        x+=1
print(x)