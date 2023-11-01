heights = [1,1,4,2,1,3]
s=sorted(heights)
p=0
for i in range(len(heights)):
    if heights[i]!=s[i]:
        p+=1
print(p)        
        