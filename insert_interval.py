intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
res=[]
intervals.sort(key =lambda x: x[0])
newInterval.sort()
for i in intervals:
    
    if not res and i[1]<newInterval[0] :
        res.append(i)
    elif  i[0]<=newInterval[1]:
        newInterval[0] = min(newInterval[0], i[0])
        newInterval[1] = max(newInterval[1], i[1])    
    else:
        res.append(newInterval)
        res.append(i)
        newInterval=[]
if newInterval:
    res.append(newInterval)        
print(res)    
# for i in range(len(intervals)):
#     if newInterval [1] < intervals[i][0]:
#         res.append(newInterval)
#         #print(res + intervals[i:])
#     elif newInterval[0]>intervals[i][1]:
#         res.append(intervals[i])
#     else:
#         newIntervals=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]  
# res.append(newInterval)
# print(res)                


    