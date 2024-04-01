num1 = "1+-1i"
num2 =  "1+-1i"
#Output: "0+2i"
#Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i,
# and you need convert it to the form of 0+2i.
# num1=1+1i , num2=2+-1i
# a1=1 , a2=2 , b1=1, b2=-1

# Basic Math:-)

# For real = a1a2-b1b2
# For complex = a1b2+a2b1
# Complex number = real+complex*(i)
n1=num1.split('+')
n2=num2.split('+')
num1_real = int(n1[0])
num1_imaginary = int(n1[1][:-1])  # Removing the 'i' at the end
num2_real = int(n2[0])
num2_imaginary = int(n2[1][:-1])

res_real=num1_real*num2_real-num1_imaginary*num2_imaginary
res_ima=num1_real * num2_imaginary + num1_imaginary * num2_real

res=str(res_real)+'+'+str(res_ima)+'i'
print(res)