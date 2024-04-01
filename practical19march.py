#append
# li=[10,20,30,40]
# li.append(41)
# print(li)

#extend
# li=[10,20,30,40]
# li.extend([24,88,68])
# print(li)

#insert
# l1=[10,20,30,40]
# l1.insert(1,8)
# print(l1)

#removal element
#pop
# l2=[10,88,'virat','srk','cristiano',10.88]
# l2.pop()
# print(l2)

#pop indexing
# l2.pop(1)
# print(l2)

#remove
# l3=[10,88,'virat','srk','cristiano',10.88]
# l3.remove('srk')
# print(l3)

#sort
# l4=[10,88,10.88,74,58]
# l4.sort()
# print(l4)

#sort desending
# l4=[10,88,10.88,74,58]
# l4.sort(reverse=True)
# print(l4)

#Properties of list
#1 list is a mutable data structure
#2 by using slicing we can accsess the specific part of list
#3 list can store hetrogeneous data types
#4 list can have duplicate element
#5 list maintain insertion order
#6 it is denoted by []
#7 list allow indexing

# user=input("enter a element:")
# l4=[10,88,77,52]
# # for i in l4:
#     if i==user:
#         print("element is present in list")
#     else:
#         print("element not in list")
        
        
# if user in l4:
#     print("present")       
# else:
#     print('not present')    
    
# user = int(input("enter an element:"))
# l4 = [1,8,55,99,63]
# for i in l4:
#     if i == user:
#         print("element is present in list")
#     else:
#         print("element not in list")

li=[11,[23,4,[34,65],[65,6],9],70]

print(li[1][0])
print(li[1][2][0])
print(li[1][4])
print(li[1][2][1])
