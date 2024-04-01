# input= "112358"
# s=int(input)
# for i in range(len(input)-1,-1,-1):
#     print(s[i])

input_str = "112358"
s=int(input_str)
for i in range(len(s) - 1, -1, -1):
    print(s[i-1]+s[i-2])

