words = ["abcw","baz","foo","bar","xtfn","abcdef"]
s=[]

ans=0
for i in range(len(words)):
    s.append(set(words[i]))
print(s)  
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if not (s[i] & s[j]):
            if ans<(len(words[i])*len(words[j])):
                ans= len(words[i])*len(words[j])
print(ans)     