# #from keys create a new dictionry from specific keys and value
# # d={}
# # l=int(input("enter len:"))
# # for i in range(l):
# #     keys=input("enter a key:")
# #     value=input("enter a value:")
# #     d[keys]=value
# # print(d)    

# #write a script to concetanate following dictionary to create new
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}

# dic4={}
# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)

# #write script to check weather a given key already exist in dict
# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# keys=2
# if keys in d:
#     print(True)
    
# #write program to iterate over dictuonaries
# for k,v in d.items():
#     print(k)
#     print(v)    
    
# #write a program to genrate dict that contain no in form of x: x*x
# n=5
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)    
        

# #write a program to add a key to dictionary
# d={1:10,2:20}
# d.update({3:30})       
# print(d)
        
# #write a python script to print dictionary where the keys are no bet
# #1 and 15 and values are square
# d={}
# for i in range(1,15+1):
#     d[i]=i*i

# print(d)        
        
# #write a script to merge two python dictionary
# d1={'a':125,'b':150,'c':170,'d':198}
# d2={'e':201,'f':210,'g':245}
# d3={}
# d1.update(d2)
# print(d1)
        
# #write a program to sum all the items in dictionary
# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# add=0
# for k,v in d.items():
#     add+=k
#     add+=v
# print(add)    
        
      
# #write program to remove key from dict
# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key=2
# d.pop(key)
# print(d)

# #write a program to map two list to a dict
# l1=[1,2,3]
# l2=[10,20,30]

# #convert two list into dict
# d={}
# li1=['ten','twenty','thirty']
# li2=[10,20,30]
# for i in range(len(li1)):
#     d[li1[i]]=li2[i]
# print(d)    
    
# #merge two python dict into one
# d1={1:10,2:20,3:30}
# d2={4:40,5:50,6:60}
# d1.update(d2)
# print(d1)

# #print the value of key 'history' from the dict
# sampledict={'class':{'student':{'name':'mike','marks':{'physics':70,'history':80}}}} 
# x=sampledict['class']['student']['marks']['history']
# print(x) #80

d={}
l1=[1,2,3]
l2=[10,20,30]     
for k,v in zip(l1,l2):
    d[k]=v
print(d)    
           
# #create a password by taking input
# #atleast 8 char and atleast 1 uppercase letter 1 speacial chr and digit
# #list tuple dict 
# #  
# import string        
# print("***password generation***") 
# print("**Password must contain at least 8 character and 1 upper case letter and 1 special character**")
# p=input("enter a password:")
# while True:
#     p=input("enter a password:")
#     if len(p)< 8:
#         print("length of password minimum 8 char")
#         continue
#     if not any(char.isupper() for char in p):
#         print("password must contain at least 1 upper letter")
#         continue
#     if not any(char.islower() for char in p):
#         print("enter atleast 1 lower character")
#         continue
#     if not any(char in string.punctuation for char in p):
#         print("password must contain at least 1 special character") 
#         continue
#     print("Your password generated successfully")
#     print(p) 
#     break
  
# if len(p)>8:
#     p_u=0
#     p_l=0
#     p_chr=0
#     p_d=0
#     for i in p:
#         if i.islower():
#             p_l+=1
#         elif i.isupper():
#             p_u+=1
#         elif i.isdigit():
#             p_d+=1
#         elif i in ['@','#','%','$','&','*','!']:
#             p_chr+=1
#     if p_l>1 and p_u>1 and p_chr>1 and p_d>1:
#         print("Your password is generated successfully") 
#     else:
#         print("your password doest fullfill all the condition")
# else:
#     print("enter at least 8 character")                                      






  
   

