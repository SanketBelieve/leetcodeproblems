nums = [1,2,3,3]
n={}
print(type(n))

for i in nums:
    if i in n:
        n[i]+=1
        print(n)
        if n[i]==len(nums)/2:
            print(i)
    else:
        n[i]=1
        print(n)  
# for i in nums:
#     if i in n:
#         n[i]+=i
#         if n[i]==len(nums)/2:
#             print(i)
        
#     else:
#         n[i]=1        
        
    
    