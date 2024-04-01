# for i in range(1,11):
#     print(i)
# for i in range(50,9,-1):
#     print(i) 
# n=10       
# for i in range(1,n):
#     print(i)    
# for i in range(n,1,-1):
#     print(i)
# for i in range(1,10):
#     if i%2==0:
#         print(i)
# for i in range(1,11):
#     if i%2==1:
#         print(i)
# s=0
# for i in range(1,11):
#     if i%2==0:
#         s+=i  
# print(s)
# p=1
# for i in range(1,11):
#     if i%2==1:
#         p=p*i                                
# print(p)
# f=9
# ans=1
# for i in range(1,f+1):
#     ans*=i
# print(ans)    
# fibbo=10
# n1,n2=0,1
# for i in range(0,fibbo):
#     if i<=1:
#         result = i
#     else:
#         result = n1 + n2
#         n1= n2
#         n2= result
    
#     print(result)
        
# m=10
# table=[]
# for i in range(1,10+1):
#     s=m*i
#     table.append(s)
# print(table)        

# d='1234'
# e=''
# for i in range(len(d)):
#     e = d[i] + e
# print(e)
    
# n5=1234
# temp = n5
# count = 0

# while temp!=0:
#     temp //=10
#     count +=1
# print(count)

# n1=1234


# n6 = 12734
# temp = n6
# res = 0
# while temp!=0:
#     rem = temp%10
#     res = res*10 + rem
#     # print(res)
#     temp//=10
# print(res)  

# for i in range(1,4):
    
#     for j in range(i,4):
#         print(j*i)
# d=input("enter a list:")
# p=d.split( )
# s=[int(i) for i in p]
# print(s)
# d=int(input("enter:"))
# li=[]
# for i in range(d):
#     l=int(input("enter no:"))
#     li.append(l)
# print(li)


# li=[10, 20, 30, 88, 96]
# n=int(input("enter:"))
# for i in li:
#     if i==n:
#         li.remove(i)
# print(li)        

#build in functions
#min,max,sum,len,sorted
# l=[10,50,89,72,71]
# print(max(l))
# print(min(l))
# print(len(l))
# print(sorted(l,reverse=True))

#[1,8,9,3,4,8]
#print the index of all the element
#write all the menthods on notebook

n = 5

# Upper half of the butterfly
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# Lower half of the butterfly
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
        