points = [[8,7],[9,9],[7,4],[9,7]]
points.sort()
res=0
for i in range(len(points)-1):
    res=max(res,points[i+1][0]-points[i][0])
print(res)    