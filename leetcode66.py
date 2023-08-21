#def plusOne( digits: list[int]) -> list[int]:

list = input("enter a list:")
list = list.split(",")
list = [int(num) for num in list]
for i in range(len(list)):
    if list[i]!= 9:
        list[i]+=1
    else:
        list.replace(1,0)
print(list)            
        
       
    
#a= list[-1]
#a= a+1
#list[-1]=a
#print(list)
'''
digits = int(input("enter:"))
digits=digits.split(',')

if digits[-1]!=9:
    
    digits[-1]+=1
    print(digits)
     

else:
    digits=digits[::1]
    digits.append(0)
    print(digits)    
'''
                
