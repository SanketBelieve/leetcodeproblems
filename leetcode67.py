def addBinary(a, b):
    # Convert binary strings to integers
    num1 = int(a, 2)
    num2 = int(b, 2)
    
    # Add the integers
    sum = num1 + num2
    
    # Convert sum back to binary string
    binary_sum = bin(sum)[2:]
    
    return binary_sum


    

