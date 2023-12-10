matrix = [[1,2,3],[4,5,6],[7,8,9]]
#output=[[7,4,1],[8,5,2],[9,6,3]]
t=[]
for i in range(len(matrix)):
    
    for c in range(i,len(matrix)):
        matrix[i][c],matrix[c][i]=matrix[c][i],matrix[i][c]
   
for i in range(len(matrix)):
    matrix[i].reverse()        
print(matrix)    