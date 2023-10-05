#def majorityElement( nums: list[int]) -> list[int]:
   # o=[]
    #p=(len(nums)/3)
nums=[1,2]
p=(len(nums)/3)
o=[]
e_cnt={}
for i in nums:
    count=0
    for j in nums:
        if i == j:
            count+=1
    e_cnt[i]=count        
print(e_cnt) 
for e_cnt, count in e_cnt.items():
    if count > p:
        o.append(e_cnt)
        print(o)
        