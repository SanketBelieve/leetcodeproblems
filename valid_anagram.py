s = "a"
t = "ab"
n=len(s)
m=len(t)
for i in range(n):
    for j in range(m):
        
        if s[i] not in t:
            print(False)
            break
        if t[j] not in s:
            print(False)
            break
    else:
        print(True)
    
    