'''
n=5
result = []
for i in range (n+1):
    r= i+1
    result.append(r)

print(result) '''
def generate(numRows: int) -> list[list[int]]:
        result = []
        result.append([1])
        for i in range(numRows-1):
            newrow=[1]
            for j in range(i):
                newrow.append(result[i][j]+result[i][j+1])
            newrow.append(1)
            result.append(newrow)    

        return result      
print(generate(5))    