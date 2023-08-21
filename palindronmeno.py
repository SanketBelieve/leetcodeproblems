
n = int(input("Enter a no:"))
reverse, temp = 0, n
while temp>0:
    reverse = reverse *10 + temp%10
    temp = temp//10
if reverse==n:
    print("this no is palindrome")
else:
    print("this no is not palindrome")       

#Recrusive method
