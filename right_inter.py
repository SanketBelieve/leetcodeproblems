intervals = [[1,4],[2,3],[3,4]]
#Output: [-1,0,1]
#print(sorted(intervals))
# s=[]
# for i in range(len(intervals)):
#     found=False
#     for j in range(i+1,len(intervals)):
        
#         if intervals[j][0] > intervals[i][1]:
            
#             s.append(i)
#             found=True
#             break
#     if not found:
#         s.append(-1)
# print(s) 
arr=[2,5,1,2,3]        
k=3   
dp=[0]*k
dp[0]=arr[0]
print(dp)
