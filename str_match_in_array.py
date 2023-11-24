words = ["mass","as","hero","superhero"]
ans=[]
for i,j in enumerate(words):
    print(i)
    print(j)
    other_word=" ".join(words[:i]+words[i+1:])

    
    if j in other_word:
        ans.append(j)
     
print(ans)  



