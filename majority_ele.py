#def majorityElement( nums: list[int]) -> list[int]:
   # o=[]
    #p=(len(nums)/3)
# num=[1,2,2,3]
# p=(len(nums)/3)
# o=[]
# d={}
# e_cnt={}
# for i in nums:
#     count=0
#     for j in nums:
#         if i == j:
#             count+=1
#     e_cnt[i]=count        
 
# for e_cnt, count in e_cnt.items():
#     if count > p:
#         o.append(e_cnt)
#         print(o)

nums = [2, 2, 1, 1, 1, 2, 2]

# Create an empty dictionary to store counts
counts = {}
s=[]
# Iterate through the list
for num in nums:
    # If the number is already in the dictionary, increment its count
    if num in counts:
        counts[num] += 1
    # If the number is not in the dictionary, add it with a count of 1
    else:
        counts[num] = 1

max_key = max(counts, key=counts.get)
s.append(max_key)
print(s)
         