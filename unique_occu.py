arr = [1,2,2,1,1,3]

s={}
for i in range (len(arr)):
    if arr[i] not in s:
        s[arr[i]]=1
    else:
        s[arr[i]]=s[arr[i]]+1
print(len(set(s.values()))==len(s.values()))       
        
        