def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    lst=[]
    set_nums=set(nums)
    for i in range(1,len(nums)+1):
        if i not in set_nums:
            lst.append(i)
        return lst    

    