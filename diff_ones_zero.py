grid = [[0,1,1],[1,0,1],[0,0,1]]
#diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0 

m, n=len(grid),len(grid[0])
# onesrow,onescol=[0]*m,[0]*n
# for i in range(m):
#     for j in range(n):
#         if grid[i][j]==1:
#             onesrow[i]+=1
#             onescol[j]+=1
# for i in range(m):
#     for j in range(n):
#         grid[i][j]=onesrow[i]+onescol[j]-(m-onesrow[i]+n-onescol[j])
# print(grid)                    
 
for i in range(m):
    for j in range(n):
        print(grid[i])
        print(grid[j])