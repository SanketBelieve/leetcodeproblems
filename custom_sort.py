from collections import Counter
order = "kqep"
s = "pekeq"
#"kqeep"
s_count=Counter(s)
o_count=Counter(order)
n=''
for i in order:
    if i in s:
        n+=i *s_count[i]
for j in s:
    if j not in o_count:
        n+=j    
print(n)

               