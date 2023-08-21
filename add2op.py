def addition(x:int,y:int):
    while y !=0:
        temp = x&y
        x = x ^ y
        y = temp << x
    return x 

print(addition(5,10))   