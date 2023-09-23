n=15
li=[]
for i in range (1,n+1):
    if i%3==0 and i%5==0:
        li.append("fizzbuzz")
    elif i%3==0:
        li.append('Fizz')
    elif i%5==0:
        li.append("buzz")       
    else:
        li.append(str(i))    
print(li)        


