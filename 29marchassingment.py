# class Student:
#     def learning(self):
#         print("he needs to learn")
#     def exam(self):
#         print("he need to appear for an exam")
# s1=Student()
# s1.name='Alex'
# s1.roll=101 
# s1.marks=94

# s2=Student()
# s2.name='Mike'
# s2.roll=102
# s2.marks=96   
# print("Student Information")
# print(s1.name) 
# print(s1.roll)
# print(s1.marks) 
# s1.learning()
# s1.exam()

# print("S2 Information")
# print(s2.name) 
# print(s2.roll)
# print(s2.marks) 
# s2.learning()
# s2.exam()
# print("*********************")

# class Laptop:
#     def keyboard(self):
#         print('it has keyboard')
#     def screnn(self):
#         print("it has screen") 
# hp=Laptop()
# hp.price=60000
# hp.color='White'
# hp.ram='8GB'
# hp.processor='i5'
           
# dell=Laptop()
# dell.price=80000
# dell.color='Orange'
# dell.ram='16GB'
# dell.processor='i7'

# lenovo=Laptop()
# lenovo.price=55000
# lenovo.color='black'
# lenovo.ram='8GB'
# lenovo.processor='AMD'
# lenovo.touchpad='Yes'
# print("*****HP INFO*****")
# print(hp.color)
# print(hp.price)
# print(hp.ram)
# print(hp.processor)
# hp.keyboard()
# hp.screnn()
# print("*****DELL INFO*****")
# print(dell.color)
# print(dell.price)
# print(dell.ram)
# print(dell.processor)
# dell.keyboard()
# dell.screnn()
# print("******Lenovo Info*******")
# print(lenovo.color)
# print(lenovo.price)
# print(lenovo.ram)
# print(lenovo.processor)
# print(lenovo.touchpad)
# lenovo.keyboard()
# lenovo.screnn()

# class Car:
#     def steering(self):
#         print("car has steering")
#     def horn(self):
#         print("car has horn")
# bmw=Car()
# bmw.color='black'
# bmw.sunroof='yes'

# audi=Car()
# audi.color="Red"
# audi.sunroof="Yes"

# tesla=Car()
# tesla.color='White'
# tesla.sunroof='Yes'        
# print("****BMW INFO****")
# print(bmw.color)
# print(bmw.sunroof)    
# bmw.horn()
# bmw.steering()
# print("***audi Info****")
# print(audi.color)
# print(audi.sunroof)
# audi.steering()
# audi.horn()
# print("***tesla Info****")
# print(tesla.color)
# print(tesla.sunroof)
# tesla.horn()
# tesla.steering()

#reverse the string
# a='Ethen'
# s=''
# for i in range(len(a)-1,-1,-1):
#     s+=a[i]
# print(s)
# s2=' '
# for i in a:
    
#count the appearance of each element in str
# a='pythonprograming'   
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)            

a='restart'
x=''
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]==a[j]:
            x=a.replace(a[j],'$')
print(x)

# for i in a:
#     if i not in x:
#         x+=i
#     else:
#         x+='$'                
# print(x)
# p=''
# for i in range(len(a),-1,-1):
#     if a[i] not in p[i]:
#         p+=a[i]
#     else:
#         p+='$'
# print(p) 
                        
# s='restart'
# s1=s[1:]
# print(s1)
# s2=''
# s2=s1.replace(s[0],'$')
# print(s2)
# s3=s[0]+s2
# print(s3)

# k='restart'
# first_le=k[0]
# w=k[1:]
# w1=''
# for i in range(1,len(k)):
#     if k[0]==print(k[i]):
#         w=w.replace(k[i],'$')
#         w1=first_le+w
# print(w1)        
        
#count char digit and symbol in string

# s="sfdghb1254#$%"

# digit=0
# chr=0
# symbol=0
# for i in s:
#     if i.isdigit():
#         digit+=1
#     elif i.isalpha():
#         chr+=1
#     else:
#         symbol+=1
# print(digit)
# print(symbol)
# print(chr)                
word='restart'
first_letter = word[0]  # Get the first letter
rest_of_word = word[1:]  # Get the rest of the word
    
# Replace all occurrences of the first letter in the rest of the word with '$'
modified_word = first_letter + rest_of_word.replace(first_letter, '$')
print(modified_word)








