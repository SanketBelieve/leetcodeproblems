
def selfDividingNumbers(self, left: int, right: int) -> list[int]:
    ls=[]
    for i in range(left,right+1):
        if '0' not in str(i) and all(i % int(digit) == 0 for digit in str(i)):
            ls.append(i)

    return ls   
        
        
        
