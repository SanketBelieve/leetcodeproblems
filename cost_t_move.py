position = [2,2,2,3,3]
odd=0
even=0

for i in position:
    if i%2==0:
        even+=1
    else:
        odd+=1  
print(min(even,odd))
        