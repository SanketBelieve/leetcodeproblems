'''list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
for i in list1:
    for j in list2:
        if i==j:
            print(list1.index(i)+list2.index(j))
            #print(min(id))'''
def findRestaurant( list1: list[str], list2: list[str]) -> list[str]:
        res = len(list1)+len(list2)
        ans = {}
        x = []
        for word in list1:
            if word == " ":
                continue
            if word in list2:
                ln = list1.index(word)+list2.index(word)
                res = min(res,ln)
                ans[word]=ln
        
        for key, val in ans.items():
            if val==res:
                x.append(key)           
        return x
    

    