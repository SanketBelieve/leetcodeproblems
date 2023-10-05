'''ops = ["5","2","C","D","+"]
sc=[]

for i in ops:
    if i=='c':
        sc.pop()
    elif i=='D':
        sc.append(sc[-1]*2)  
    elif i=='+':
        sm=sc[-2]+sc[-1]
        sc.append(sm) 
    else:
        sc.append(int(i))      
print(sc)  
print(sum(sc))  '''

def calPoints( operations: list[str]) -> int:
        lst=[]
        for i in operations:
            if i=="C":
                lst.pop()
            elif i=="D":
                lst.append(lst[-1]*2)
            elif i=="+":
                sm=lst[-2]+lst[-1]
                lst.append(sm)
            else:
                lst.append(int(i))
        print(lst)
        return sum(lst)   
    
print(calPoints(["5","2","C","D","+"]))     