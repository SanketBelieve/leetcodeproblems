
# arr = [0,1,2,3,4,5,6,7,8]
# a=[]
# b=[]
# for i in arr:
#     if i%2==0:
#         a.append(i)
#     else:
#         b.append(i)    
# a.sort()
# b.sort()
# print(a+b)

def sortByBits(arr: list[int]) -> list[int]:
        return sorted(arr,key=lambda x: (bin(x).count("1"),x))
    



