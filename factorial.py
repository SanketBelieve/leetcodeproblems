num = int(input("enter a no:"))
facterial = 1

if num<=0:
    print("facterial of negative no can not be calculated")
elif num == 1:
    print("factrerial of 1 is 1")
else:    
    for i in range(1,num+1):    
        facterial = facterial*i
    print("facterial of",num,"is",facterial)            
            