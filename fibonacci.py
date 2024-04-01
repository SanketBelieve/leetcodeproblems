n = int(input("Enter a number: "))
first ,second = 0 ,1
print("the fibbonacci series are")
for i in range(0,n):
    if i<=1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    if result > n:
        break
    print(result)
    
        
# n=10

# def fib():
#     a,b = 0,1
#     while a<10:
#         yield a
#         a,b = b,a+b
        
# a = fib()
# for i in range(10):
#     print(a.__next__())     