#properties
#1 it is mutable in nature
#2 it is denoted by {} and it has key and value pair
#3 key's are unique and immutable
#4 it allow hetrogeneous data type
#5 it does not support slicing and indexing
#6 from python version 3.6 onwords it maintain insertion order
#7 it allow duplicate values but not keys




# d={'a':101,'b':102,'c':103,'d':104,'e':105}
# d['g']=108
# print(d)
# d['d']=107
# print(d)

#sets Methods
#mathematical operations
#1 Union
a={10,20,30,70}
b={40,50,60,70}
# print(a.union(b))
# print(a | b)

#intersection
#return the common element from both the sets
# print(a.intersection(b))
# print(a & b)

#Differance method return the element that in set a
# print(a.difference(b))
# print(a - b)

#symetric differance
#return the uncommon element from both the sets
# print(a.symmetric_difference(b))
# print(a ^ b)



#frozen set
# li=[1,8,66]
# li2= frozenset(li)
# s= {'o','uu',99,li2}
# print(s)


#iterating nasted list
# mh=['mumbai','pune']
# gj=['surat','rajkot']
# india = [mh,gj]

# for state in india:
#     for city in state:
#         print(city)

# s={1,8,9,55}
# q={4,12,9,63,55}
#s.add(52)

#print(s)
# s.difference(q)
# s.difference_update(q)
# print(s)

#discard method dlete the specific element from set
# s.discard(55)
# print(s)


#intersection update
s={1,8,9,55}
q={4,12,9,55}
# s.intersection_update(q)
# print(s)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# x &= y
# print(x)

#disjoint() if both sets has no common element
# in between then it return True
# s={1,8,15}
# q={4,12,9,55}
# print(s.isdisjoint(q))

#issuperset() 
#The issuperset() method returns True if all items in the specified
# set exists in the original set, otherwise it returns False.

#As a shortcut, you can use the >= operator instead, see example below.
#subset 
#The issubset() method returns True if all items in the set exists in the
# specified set,
# otherwise it returns False.
#As a shortcut, you can use the <= operator instead, see example below.
a={1,2,3}
b={1,2,3,4,5}
print(b.issuperset(a))
print(a.issubset(b))

s={1,8,88}
#d=s.clear()
#copy return the copy of the set in new variable
d=s.copy()
print(d)


#pop removes the any random element from set
set1={22,9,5,77,39}
set1.pop()
print(set1)

#remove 
#removes the specific element from sets
set1.remove(77)
print(set1)


#symetric_differance_update
#return the uncommon element from both the sets
s={1,8,9,55}
q={4,12,9,55}
p=s.symmetric_difference(q)
print(p)