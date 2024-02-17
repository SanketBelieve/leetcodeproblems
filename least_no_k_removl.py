from collections import Counter
arr = [5,5,4]
k = 1
d=Counter(arr)
print(d)
sorted_d=sorted(d.items(),key=lambda x:x[1])
print(sorted_d)
for i,c in sorted_d:
    print(c)
    if k>=c:
        k-=c
        del d[i]
    else:
        break

print(len(d))
        
# s=set(arr)
# for i in arr:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i]=1
# min_heap = []
# for num, freq in d.items():
#     heapq.heappush(min_heap, (freq, num))

# # Remove the least frequent element from the set till k becomes zero
# while k > 0 and min_heap:
#     freq, num = heapq.heappop(min_heap)
#     if num in s:
#         s.remove(num)
#         k -= 1  
# print(len(s))               