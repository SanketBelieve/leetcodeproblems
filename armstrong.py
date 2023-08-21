num = int(input("Enter a no: "))
count = len(str(num))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp //= 10
    
if num == sum:
    print("Given no is armstrong no")
    
else:
    print("Given no is not a armstrong no:")        
    
    
