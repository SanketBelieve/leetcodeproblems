nums = [1,1,1,1]
minK = 1
maxK = 1
subl=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        subl.append(nums[i:j])
print(subl)
cnt=0      
for i in subl:
    if min(i)==minK and max(i)==maxK:
        cnt+=1
print(cnt)      
        