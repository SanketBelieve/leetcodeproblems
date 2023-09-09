from itertools import combinations
def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        mylist=[]
        for i in combinations(range(1,10),k):
            if sum(i)==n:
                mylist.append(i)
        return mylist        
