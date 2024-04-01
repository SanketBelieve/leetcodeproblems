# t=tuple()
# print(t,type(t))
# t=('a','b','c','d','e')
# print(t[0])
# print(t[1])
# print(t[2])
# print(t[3])
# print(t[4])

#negative indexing
# print(t[-1])
# print(t[-2])
# print(t[-3])

#if tuple consist a single element then giving quama is mandatory
#otherwise it will read value's data type
#p=(1)
#data type of p is int
#p=(1,)
#data type of p is tuple
# t=('a','b','c','d','e','f','g','h','i','e','c','e')
# #indexing
# print(t[0:5:1])

# print(t[2:8:1])

# print(t[-1:-7:-1])

# print(t[:5:])

# print(t.index('c'))

# print(t.count('e'))

#li=list(t)
# li.remove('d')
# print(li)

# t=tuple(li)
# print(t)


# t=(52,85,89,78,52,52)
# print(t[0:2])
# print(t.count(52))
# print(t.index(52))

# print(t[::-1])

import math
x=53.2
#ceil and floor are the math module that used in python
print(math.floor(x)) #print nearest smallest int than x
print(math.ceil(x)) #print nearest bigger int that x

#write a program to compute element wise sum of given tuple
# t1=(1,2,3,4)
# t2=(3,5,2,1)
# t3=(2,2,3,1)
# # op-(6 9 8 6)
# t1=list(t1)
# t2=list(t2)
# t3=list(t3)
# res=[]
# for i in range(len(t1)):
#     s=t1[i]+t2[i]+t3[i]
#     res.append(s)
# print(tuple(res))

#write a python program to find repeated items in a tuple

# t=(1,4,5,6,4,44,55,77,88,99,2,4,6,2,4,6,2,3,4,6,2,6,2,6,2)
# t=list(t)
# t.sort()
# t6=[]
# for i in range(len(t)-1):
#     if t[i]==t[i+1]:
#         t6.append(i)
# print(tuple(t6))    
    
#write a python program to check if a specified element appears
#a tuple of tuples
#t=(('red','white','blue'),('green','pink','purple'),('orange','yellow','lime'))
#color1='green'
color2='white'
color3='olive'
# for i in t:
#     for j in i:
#         if j==color1 or j==color2 or j==color3:
#             print(True)
#         elif j!=color1 or j!=color2 or j!=color3:
#             print(False)
#delete duplicate from list
# li=[1,4,5,6,4,44,55,77,88,99,2,4,6,2,4,6,2,3,4,6,2,6,2,6,2]
# l2=[]
# for i in li:
#     if i not in l2:
#         l2.append(i)
# print(l2)  
# def color(t,color1):
    
#     for i in t:     
#         if color1 in i:
#             return True
             
#         else:
#             return False
# t=(('red','white','blue'),('green','pink','purple'),('orange','yellow','lime'))    
# color1='olive'        
# print(color(t,color1))           

# for i in t:     
#     if color1 in i:
#         print(True)
#         break
        
#     else:
#         print(False)
#         break


# li=['p','o','j','.','n','r']
# print(tuple(li))

#sort the tuple by its float element
t=(('item3','24.3'),('item1','12.20'),('item2','15.10'))
sorted(t , key=lambda x: float(x[1]))
print(t)
# l=[]
# for i in t:
#     for j in i:
#         l.append(j)
# print(sorted(l,reverse=True))        
# l.sort(reverse=True)   
# print(l)
# n=[]
# for i in range(len(l)//2):
#     n.append((l[i],l[i+3]))
# print(n)    
# print(tuple(n))

#find max no from list without using function and method
# li=[1,4,5,6,4,44,55,77,88,99,2,4,6,2,4,6,2,3,4,6,2,6,2,6,2]
# #print(max(li)
# f=0
# for i in range(len(li)-1):
#     if li[i]>f:
        
#         f=li[i]
# print(f)           

#remove empty element from list
# li=['hello',3.14,'','',40]

# print(li)
# for i in range(len(li)-1,-1,-1):
#     if li[i]=='':
#         li.remove(li[i])
# print(li)
#remove 0,4,5 index element        
# li=['red','Green','White','Black','Pink','Yellow']
# l2=[]
# for i in range(len(li)):
#     if i in (0,4,5):
#         l2.append(li[i])
# print(l2)        
        
        
li=[11,22,33] #112233
l2=''
for i in range(len(li)):
    l2+=str(li[i])
print(l2)         
        