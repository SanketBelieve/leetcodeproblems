head = [1,2,3,4,5]
k = 2
s=[]
# while k>0:
#     for i in head:
#         s.insert(0,i)
#     k-=1
# print(s)          
effective_rotations = k % len(head)
print(effective_rotations)

# Rotate the elements of the list to the left by effective_rotations positions
rotated_head = head[-effective_rotations:] + head[:-effective_rotations]

print(rotated_head)       