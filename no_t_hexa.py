def toHex(self, num: int) -> str:
        res=[]
        dic = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        if num ==0:
            return "0"
        if num < 0:
            num=num+2**32
        while num>0:
            digit = num%16
            num = num // 16
            if digit > 9 and digit <16:
                digit = dic[digit] 
            else:
                digit=str(digit)    
            res.append(digit)
        return "".join(res[::-1])
