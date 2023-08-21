num = int(input("enter a no:"))
sum = 0
for i in range(1,(num//2)+1):
    remainder = num % i
    if remainder == 0:
        sum = sum + i
if sum == num :
    print("This is a perfect no")
else:
    print("this is not perfect no")            
        
    