nums = [1,2,3,1,2,3,1,2]
k = 2
l=0
res=0
d={}
# for i in range(len(nums)):
#     d[nums[i]] += 1
#     while d[nums[i]]<k:
#         d[nums[l]]-=1
#         l+=1
#     res=max(l,i-l+1)
# print(res)    

# for i in range(len(nums)):
#     for i in 
#     if nums[i] not in lst:
#         lst.append(nums[i])
# print(lst)        
        
for i in range(len(nums)):
    if nums[i] in d:
        d[nums[i]] += 1
    d[nums[i]] =0 
    
    while min(d.values()) < k:
        d[nums[l]] -= 1
        if d[nums[l]] == 0:
            del d[nums[l]]
        l += 1
        
    res = max(res, i - l + 1)
print(res)        
    
    
    
