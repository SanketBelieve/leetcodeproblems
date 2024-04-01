
points = [[10,16],[2,8],[1,6],[7,12]]
points.sort()
arrow=1
end=points[0][1]
if not points:
    print(0)
for i in points[0:]:
    if i[0] > end:
        arrow+=1
        end=i[1]
    else:
        end=min(end,i[1])    
print(arrow)