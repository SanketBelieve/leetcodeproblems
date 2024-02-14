matrix = [[1,2],[1,3]]
k = 2
s=[]

for i in matrix:
    s.extend(i)
s.sort()
print(s[k-1])     