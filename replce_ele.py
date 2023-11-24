n=14
p=0
# for i in range(a+1):
#     print(i)
#     s=i//2
#     p.append(s)
# #n=list(set(p))    
# print(p)
   
    
while n > 0:
    if n % 2==0:
        n/=2
        p+=1
        
    else:
        n -= 1
        p += 1
print(p)   
