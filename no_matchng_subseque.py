s = "abcde"
words = ["a","bb","acd","ace"]
words.sort()
c=0
for i in range(len(words)):
    for j in range(len(s)):
        if words[i]==s[j]:
            c+=1
print(c)            