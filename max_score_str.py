# s = "011101"
# l=-1
# zero=0
# one=0
# for i in range(len(s)-1):
#     if s[i]=='0':
#         zero+=1
#     else:
#         one+=1
        
#     l=max(l,zero-one) 
# one+=s[-1]=='1' 
# print(l+one)   
n=15      
for i in range(1,n):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
        continue
    elif i%3==0:
        print('Fizz')
        continue
    elif i%5==0 :
        print('FizzBuzz')
        continue
    else:
        print(i)