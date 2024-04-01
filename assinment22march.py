#Exersize1 add a list of element to a list
# set1={'yellow','orange','black'}
# li1=['blue0','green','red']
# set1.update(li1)
# print(set1)


# #return a list of identical items from two sets
# set2={10,20,30,40,50}
# set3={30,40,50,60,70}

# print(set2.intersection(set3))


# #get only unique items from two sets  
# set4={10,20,30,40,50}
# set5={30,40,50,60,70}
# print(set4.union(set5))

# #given a list of numbers , write a python program to count positive
# #and negative no in list
# list1=[1,-8,99,-25,-89,45,98]
# pos=0
# neg=0
# for i in list1:
#     if i >=0:
#         pos+=1
#     else:
#         neg+=1
# print(pos)
# print(neg)            

# #update the first set with item that don't exists in the second set
# s1={10,20,30}
# s2={20,40,50}
# s1.difference_update(s2)
# print(s1)

# #remove items from set at once
# s3={10,20,30,40,50}
# s8=[10,30,20]
# for i in s8:
#     if i in s3:
#         s3.remove(i)
# print(s3)

#return the set of elements present in set A or B but not both
# s5={10,20,30,40,50}
# s6={30,40,50,60,70}
# s5.symmetric_difference_update(s6)
# print(s5)


# s={}
# cnt=int(input("how much dict element:"))

# for i in range(cnt):
#     d1=input("enter key:")
#     d2=input("enter value:")
#     s[d1]=d2
# print(s)

li=[['aa','bb'],['cc','dd']]
li2=[]
for i in li:
    for j in i:
        li2.append(j)
print(li2)        

li1=[10,20,[300,400,[5000,6000],500],30,40]
li1[2][2].append(7000)
print(li1)
