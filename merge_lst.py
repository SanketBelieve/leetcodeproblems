intervals = [[1,3],[2,6],[8,10],[15,18]]
n=len(intervals)
l=[]
intervals.sort()
print(intervals)
for i in sorted(intervals):
    if l and i[0] <= l[-1][1]:
        l[-1][1] = max(l[-1][1], i[1])
    else:
        l.append(i)
print(l)              
# for i in range(n-1):
#     if intervals[i][1] >= intervals[i+1][0]:
#         l.append([[i][0],[i+1][1]])
# print(l)     
    