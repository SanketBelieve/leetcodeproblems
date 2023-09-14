num=[9,6,4,2,3,5,7,0,1]
n=set(num)

for i in range (0,max(n)):
    if i not in n:
        print(i)