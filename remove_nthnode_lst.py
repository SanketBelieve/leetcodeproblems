head = [1,2]
n = 1

head.sort()
for i in range(-1,-len(head)-1,-1):
    if i==-n:
        head.remove(head[i])
print(head)