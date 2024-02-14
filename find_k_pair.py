
nums1 = [1,2,4,5,6]
nums2 = [3,5,7,9]
k = 3
s=[]
for i in nums1:
    for j in nums2:
        s.append([i,j])
print(s)
s.sort()
# n=[]
# for i in range(k):
#     n.append(s[i])
