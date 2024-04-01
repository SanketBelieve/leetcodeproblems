
#Class 
#there are 3 ways to define class
#class class_name(objname):
#class is blueprint or templete for creating object
#object is a instance of class   
    #pass
# class classname('objnme'):
#     pass  
  
# class class_nm():
#     pass
# class class_nme:
#     pass
    
# class A:
#     x=10
# a1=A()
# a1.y=20
# print(a1.x)
# print(a1.y)        

# a2=A()
# a2.x=30
# print(a2.x)
# print(a2.y) #attribute error

#convert uppercase to lowercasee
# str1="ADHYAYAN"
# op=str1.lower()
# print(op) #adhyayan

# #find the index position and occurance of 'D' in string
# str1="ADHYAYAN"
# print(str1.index('D'))
# print(str1.count('D'))

# #create a string made of first charcher and last charcter
# str1="ADHYAYAN"
# str2=str1[0]+str1[-1]
# print(str2)#AN

# #replace the string
# str1='I am Student' #op=i am software developer
# str2=str1.replace('Student',"software developer")
# print(str2)

# #do perform addition of all digit in str
# str1='12345'
# addition=0
# for i in str1:
#     addition+=int(i)
# print(addition)    

# #arrange the string such that lower case charcter came first
# str1='ADHYayan'
# str2=''
# for i in str1:
#     if i.islower():
#         str2+=i.upper()
#     elif i.isupper():
#         str2+=i.lower()    
# print(str2)        

# #made a string of first middle and last character
# str1='james'
# str2=''

# str2+=str1[0]+str1[(len(str1)//2)]+str1[-1]
# print(str2)
    
# #create a string of middle 3 charcter
# str1="JhonDipPeta"
# mid=len(str1)//2
# str2=''
# str2+=str1[mid-1]+str1[mid]+str1[mid+1]    
# print(str2) #Dip

# case2="JaSonAy"
# mid2=len(case2)//2
# op2=""
# op2+=case2[mid2-1]+case2[mid2]+case2[mid2+1]
# print(op2)

