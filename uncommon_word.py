s1 = "this apple is sweet"
s2 = "this apple is sour"
s=s1.split(' ')
p=s2.split(' ')
ls=[]

for i in s:
    if i not in p and s.count(i)==1:
        ls.append(i)
for j in p:
    if j not in s and p.count(j)==1:
        ls.append(j)
print(ls)