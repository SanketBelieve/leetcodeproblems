def countBits( n: int) -> list[int]:
        sum = 0
        ans =[]
        for i in range(n+1):
            sum = bin(i).count("1")
            ans.append(sum)
        return ans

print(countBits(10))    