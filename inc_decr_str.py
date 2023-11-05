s="aaaabbbbcccc"
# s=list(s)
# p=""
# for i in set(s):
#     print(i)
#     p+=i
# print(p)
      
s=list(s)
result=""
while s:
    for i in sorted(set(s)):
        s.remove(i)
        result+=i
    for i in sorted(set(s),reverse=True):
        s.remove(i)
        result+=i    
print(result)    