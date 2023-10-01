
s = "Let's take LeetCode contest"
p=[]

n=s.split()

for i in n:
    l=(i[::-1])
    p.append(l)
output=' '.join(p)
print(output)
    
    
