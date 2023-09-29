a = "aaa"
b = "aaa"
s=0
for i in a:
    for j in b:
        if i!=j:
            s+=1
        break       
print(s)            

def findLUSlength(self, a: str, b: str) -> int:
    if a==b:
        return -1
    if len(a)<len(b):
        return len(b)
    if len(b)< len(a):
        return len(a)
    if len(b)== len(a):
        return len(b)

def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
    