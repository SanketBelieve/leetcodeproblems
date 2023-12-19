from collections import Counter
arr = [1,2,2,6,6,6,6,7,10]
l=len(arr)
s=l//4
dic=Counter(arr)
for k,v in dic.items():
    if v > s:
        print(k)
      