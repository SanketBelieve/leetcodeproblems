# arr = [1,2,2,6,6,6,6,7,10]

# check=len(arr)//4
# for i in set(arr):
#     if arr.count(i) > check:
#         print(i)
arr = [1,2,2,6,6,6,6,7,10]

check=len(arr)//4
for i in set(arr):        
    print(arr.count(i))