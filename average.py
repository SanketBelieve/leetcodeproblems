size = int(input("enter a size:"))
arr = []
for i in range(0,size):
    elem = int(input("please give value for index "+str(i)+":"))
    arr.append(elem)
avg= sum(arr)/size
print(avg)    