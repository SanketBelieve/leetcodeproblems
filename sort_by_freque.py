s = "raaeaedere"
#p=''.join(sorted(s))
#print(p)

p={}
n=''    
for chr in s:
    if chr in p:
        p[chr]+=1
    else:
        p[chr]=1
sorted_dict = {k: v for k, v in sorted(p.items(), key=lambda item: item[1])}
for char, count in reversed(list(sorted_dict.items())):
    n+=char*count
print(n)
   