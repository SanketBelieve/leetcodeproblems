nums = [3,1,-2,-5,2,-4]
p=[]
n=[]
# r=-1
# while len(k)<len(s):
#     for i in range(len(s)):
#         k.append(s[r])
#         k.append(s[i])
#         r-=1
#         if len(k)==len(s):
#             break
#     if len(k)==len(s):
#         break    
# print(k)    
for i in nums:
    if i>=0:
        p.append(i)
    else:
        n.append(i)            
merged = []

# Determine the length of the longer list
max_length = max(len(p), len(n))

# Merge the lists alternately
for i in range(max_length):
    if i < len(p):
        merged.append(p[i])
    if i < len(n):
        merged.append(n[i])

print("Merged list:", merged)    