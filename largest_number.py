nums = [3,30,34,5,9]
res = "".join(map(str, nums))
sorted_res = sorted(res, reverse=True)
result = "".join(sorted_res)
print(result)


nums = sorted(nums,key=lambda x:x / (10 ** len(str(x)) - 1 ), reverse=True)
str_nums = [str(num) for num in nums]
res = ''.join(str_nums)
res = str(int(res))
print(res)
        