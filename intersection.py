nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
p=[]


for i in nums1:
    for j in nums2:
        if i==j:
            p.append(i)
print(list(set(p)))