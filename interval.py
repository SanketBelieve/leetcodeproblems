# intervals = [[1,2],[2,3],[3,4],[1,3]]
# intervals.sort()
# count=0
# for i in range(len(intervals-1)):
#     if intervals[i][0]==intervals[i+1][0]:
#         count+=1
#     else:
#         print(0)
# print(count)            
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals.sort()
print(intervals)
count = 0
for i in range(len(intervals) - 1):
    if intervals[i][0] == intervals[i+1][0]:  # Check for overlapping intervals
        count += 1
    else:
        print(0)  # This prints if there's no overlap, you may want to handle this case differently
print(count)
