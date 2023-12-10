matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
t=[]
for i in range(len(matrix[0])):
    temp=[]
    for c in range(len(matrix)):
        temp.append(matrix[c][i])
        
    t.append(temp)    
print(t)    
  