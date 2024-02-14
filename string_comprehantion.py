chars = ["a","a","b","b","c","c","c"]
ch=len(chars)

if ch < 2:
    print(chars)
i=j=0    
while i < ch:
    count=1
    while i< ch-1 and chars[i]==chars[i+1]:
        count+=1
        i+=1
    chars[j]==chars[i]
    j+=1
    if count > 1:
        for val in str(count):
            chars[j]=val
            j+=1
    i+=1
print(j)            
        