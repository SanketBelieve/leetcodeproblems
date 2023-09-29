'''
a=[7]
b=[7]
a=a*2
print(b.extend(a))
print(b==a.extend(b))
print((a==b.extend(b)))
'''
'''
def square(x):
    return x*x
def cube(x):
    return x * 3
def add(x,y):
    return x - y

print(square(cube(add(3,2))))
'''
'''
n=12345
total = 0
product = 1
while n != 0:
    digit = n%10
    total += digit
    product *= digit
    n//=10
print(total)
print(product + total)'''

'''
list1=[300,150,450]
list2=[]
for i in list1:
    if i <=300:
        i += 15
        list2.append(i)
    else:
        dc=0.15 * i 
        i+=dc 
        list2.append(i)

print(list2) '''


