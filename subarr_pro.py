nums = [10,5,2,6]
k = 100
res=[]
r=[]
# for i in range(len(nums)):
#     for combination in combinations(nums,i):
#         res.append(list(combination))
# print(res)        
# duct=1  
# for i in res:
#     if len(i)==0:
#         res.remove(i)
# print(res)     
# for pro in res:
#     for i in pro:
#         duct*=i
#     r.append(duct)  
#     duct=1  
 
# print(r) 
# print(res)
# print(len(r))
# print(len(res))
# d={}  
# for k,v in zip(res,r):
#     d[tuple(k)]=v
# print(d)    
# final_res=[]
# for k,v in d.items():
#     if v < 100:
#         final_res.append(list(k))
# print(final_res)
# print(len(final_res))        
   
product=1
left=0
count=0
for right,num in enumerate(nums):
    product*=num
    while product>=k:
        product/=nums[left]
        left+=1
    count += right-left+1
print(count)         
        
    