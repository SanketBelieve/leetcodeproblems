arr = [1,2,3,4,5]
k = 2
arr.sort()

n=len(arr)
median = arr[(n - 1) // 2]
res=[]
# if n%2==1:
#     med=arr[n//2]
# else:
#     med = (arr[n // 2 - 1] + arr[n // 2]) / 2    
# print(int(med)) 

# for i in range(len(arr)):
#     s=arr[i]-med
#     l.append(s)
# p=[i for i,c in sorted(zip(arr,l),reverse=True)]
# res=[]
# for i in range(k):
#     res.append(p[i])
# print(res)    
for a in arr:
    res.append([abs(a - median), a])
res.sort(reverse = True)
print([res[i][1] for i in range(k)])