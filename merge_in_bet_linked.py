list1 = [10,1,13,6,9,5]
a = 3
b = 4
list2 = [1000000,1000001,1000002]

li3=[]
# list1.pop(b)
# list1.pop(a)
del list1[a:b+1]
for i in range(len(list2)):
    list1.insert(3,list2[i])
print(list1)   